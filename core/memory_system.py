"""
MemorySystem - Stores and retrieves conversation history, patterns, and learning data
Enables agents to build on previous interactions and learn from experience
"""

import json
import time
import hashlib
from typing import Dict, List, Any, Optional, Tuple, Set
from dataclasses import dataclass, asdict
from enum import Enum
import sqlite3
from pathlib import Path
import pickle
import numpy as np
from collections import defaultdict, deque

from .reward_system import RewardScores


class MemoryType(str, Enum):
    """Types of memories stored in the system."""
    CONVERSATION = "conversation"
    PATTERN = "pattern"
    LEARNING = "learning"
    INSIGHT = "insight"
    EVOLUTION = "evolution"


@dataclass
class MemoryEntry:
    """A single memory entry with metadata and content."""
    memory_id: str
    memory_type: MemoryType
    content: Any
    timestamp: float
    agent_id: str
    depth_level: int
    reward_scores: Optional[RewardScores] = None
    tags: List[str] = None
    importance: float = 0.5
    access_count: int = 0
    last_accessed: float = None
    
    def __post_init__(self):
        if self.tags is None:
            self.tags = []
        if self.last_accessed is None:
            self.last_accessed = self.timestamp
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for storage."""
        data = asdict(self)
        if self.reward_scores:
            data['reward_scores'] = self.reward_scores.as_dict()
        return data


@dataclass
class PatternMemory:
    """A learned pattern from multiple interactions."""
    pattern_id: str
    pattern_type: str
    frequency: int
    confidence: float
    examples: List[str]
    reward_trend: List[float]
    last_observed: float
    utility_score: float


class MemorySystem:
    """
    Comprehensive memory system for storing and retrieving agent experiences.
    Supports both SQLite persistence and in-memory caching for performance.
    """
    
    def __init__(self, db_path: str = "consciousness_memory.db", 
                 max_memory_entries: int = 10000,
                 max_patterns: int = 1000):
        self.db_path = db_path
        self.max_memory_entries = max_memory_entries
        self.max_patterns = max_patterns
        
        # In-memory caches for performance
        self.conversation_cache: deque = deque(maxlen=1000)
        self.pattern_cache: Dict[str, PatternMemory] = {}
        self.insight_cache: Dict[str, MemoryEntry] = {}
        
        # Pattern recognition
        self.pattern_frequency: Dict[str, int] = defaultdict(int)
        self.reward_patterns: Dict[str, List[float]] = defaultdict(list)
        
        # Initialize database
        self._init_database()
        
        # Load existing patterns
        self._load_patterns()
    
    def _init_database(self):
        """Initialize SQLite database with required tables."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Memory entries table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS memory_entries (
                memory_id TEXT PRIMARY KEY,
                memory_type TEXT NOT NULL,
                content TEXT NOT NULL,
                timestamp REAL NOT NULL,
                agent_id TEXT NOT NULL,
                depth_level INTEGER NOT NULL,
                reward_scores TEXT,
                tags TEXT,
                importance REAL DEFAULT 0.5,
                access_count INTEGER DEFAULT 0,
                last_accessed REAL NOT NULL
            )
        ''')
        
        # Patterns table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS patterns (
                pattern_id TEXT PRIMARY KEY,
                pattern_type TEXT NOT NULL,
                frequency INTEGER DEFAULT 1,
                confidence REAL DEFAULT 0.5,
                examples TEXT NOT NULL,
                reward_trend TEXT NOT NULL,
                last_observed REAL NOT NULL,
                utility_score REAL DEFAULT 0.5
            )
        ''')
        
        # Create indexes for performance
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_memory_type ON memory_entries(memory_type)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_agent_id ON memory_entries(agent_id)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_timestamp ON memory_entries(timestamp)')
        cursor.execute('CREATE INDEX IF NOT EXISTS idx_pattern_type ON patterns(pattern_type)')
        
        conn.commit()
        conn.close()
    
    def store_memory(self, memory_entry: MemoryEntry) -> bool:
        """Store a new memory entry."""
        try:
            # Add to in-memory cache
            if memory_entry.memory_type == MemoryType.CONVERSATION:
                self.conversation_cache.append(memory_entry)
            elif memory_entry.memory_type == MemoryType.INSIGHT:
                self.insight_cache[memory_entry.memory_id] = memory_entry
            
            # Store in database
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                INSERT OR REPLACE INTO memory_entries 
                (memory_id, memory_type, content, timestamp, agent_id, depth_level,
                 reward_scores, tags, importance, access_count, last_accessed)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                memory_entry.memory_id,
                memory_entry.memory_type.value,
                json.dumps(memory_entry.content),
                memory_entry.timestamp,
                memory_entry.agent_id,
                memory_entry.depth_level,
                json.dumps(memory_entry.reward_scores.as_dict()) if memory_entry.reward_scores else None,
                json.dumps(memory_entry.tags),
                memory_entry.importance,
                memory_entry.access_count,
                memory_entry.last_accessed
            ))
            
            conn.commit()
            conn.close()
            
            # Update pattern recognition
            self._update_pattern_recognition(memory_entry)
            
            return True
            
        except Exception as e:
            print(f"Error storing memory: {e}")
            return False
    
    def retrieve_memories(self, 
                         memory_type: Optional[MemoryType] = None,
                         agent_id: Optional[str] = None,
                         depth_level: Optional[int] = None,
                         tags: Optional[List[str]] = None,
                         limit: int = 100,
                         min_importance: float = 0.0) -> List[MemoryEntry]:
        """Retrieve memories based on criteria."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            query = "SELECT * FROM memory_entries WHERE 1=1"
            params = []
            
            if memory_type:
                query += " AND memory_type = ?"
                params.append(memory_type.value)
            
            if agent_id:
                query += " AND agent_id = ?"
                params.append(agent_id)
            
            if depth_level:
                query += " AND depth_level = ?"
                params.append(depth_level)
            
            if min_importance > 0:
                query += " AND importance >= ?"
                params.append(min_importance)
            
            query += " ORDER BY importance DESC, timestamp DESC LIMIT ?"
            params.append(limit)
            
            cursor.execute(query, params)
            rows = cursor.fetchall()
            conn.close()
            
            memories = []
            for row in rows:
                memory = self._row_to_memory_entry(row)
                if memory:
                    memories.append(memory)
                    
                    # Update access count
                    memory.access_count += 1
                    memory.last_accessed = time.time()
                    self._update_memory_access(memory)
            
            # Filter by tags if specified
            if tags:
                memories = [m for m in memories if any(tag in m.tags for tag in tags)]
            
            return memories
            
        except Exception as e:
            print(f"Error retrieving memories: {e}")
            return []
    
    def get_conversation_context(self, agent_id: str, depth_level: int, 
                                context_window: int = 10) -> List[MemoryEntry]:
        """Get recent conversation context for an agent."""
        return self.retrieve_memories(
            memory_type=MemoryType.CONVERSATION,
            agent_id=agent_id,
            depth_level=depth_level,
            limit=context_window
        )
    
    def get_insights_by_topic(self, topic_tags: List[str], 
                             min_confidence: float = 0.7) -> List[MemoryEntry]:
        """Get insights related to specific topics."""
        insights = self.retrieve_memories(
            memory_type=MemoryType.INSIGHT,
            tags=topic_tags,
            min_importance=min_confidence
        )
        return sorted(insights, key=lambda x: x.importance, reverse=True)
    
    def _update_pattern_recognition(self, memory_entry: MemoryEntry):
        """Update pattern recognition based on new memory."""
        if not memory_entry.reward_scores:
            return
        
        # Create pattern key from content and context
        pattern_key = self._generate_pattern_key(memory_entry)
        
        # Update frequency
        self.pattern_frequency[pattern_key] += 1
        
        # Update reward patterns
        overall_score = memory_entry.reward_scores.overall()
        self.reward_patterns[pattern_key].append(overall_score)
        
        # Keep only recent rewards for trend analysis
        if len(self.reward_patterns[pattern_key]) > 20:
            self.reward_patterns[pattern_key] = self.reward_patterns[pattern_key][-20:]
        
        # Update pattern confidence
        if pattern_key in self.pattern_cache:
            pattern = self.pattern_cache[pattern_key]
            pattern.frequency = self.pattern_frequency[pattern_key]
            pattern.confidence = min(0.95, pattern.frequency / 10.0)
            pattern.reward_trend = self.reward_patterns[pattern_key]
            pattern.last_observed = time.time()
            pattern.utility_score = np.mean(self.reward_patterns[pattern_key])
    
    def _generate_pattern_key(self, memory_entry: MemoryEntry) -> str:
        """Generate a pattern key from memory content and context."""
        # Create a hash of content + context for pattern identification
        content_str = str(memory_entry.content)
        context_str = f"{memory_entry.agent_id}:{memory_entry.depth_level}:{memory_entry.tags}"
        combined = f"{content_str}|{context_str}"
        return hashlib.md5(combined.encode()).hexdigest()[:16]
    
    def _row_to_memory_entry(self, row) -> Optional[MemoryEntry]:
        """Convert database row to MemoryEntry object."""
        try:
            reward_scores = None
            if row[6]:  # reward_scores column
                reward_data = json.loads(row[6])
                reward_scores = RewardScores(**reward_data)
            
            tags = []
            if row[7]:  # tags column
                tags = json.loads(row[7])
            
            return MemoryEntry(
                memory_id=row[0],
                memory_type=MemoryType(row[1]),
                content=json.loads(row[2]),
                timestamp=row[3],
                agent_id=row[4],
                depth_level=row[5],
                reward_scores=reward_scores,
                tags=tags,
                importance=row[8],
                access_count=row[9],
                last_accessed=row[10]
            )
        except Exception as e:
            print(f"Error converting row to memory entry: {e}")
            return None
    
    def _update_memory_access(self, memory_entry: MemoryEntry):
        """Update memory access statistics in database."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                UPDATE memory_entries 
                SET access_count = ?, last_accessed = ?
                WHERE memory_id = ?
            ''', (memory_entry.access_count, memory_entry.last_accessed, memory_entry.memory_id))
            
            conn.commit()
            conn.close()
        except Exception as e:
            print(f"Error updating memory access: {e}")
    
    def _load_patterns(self):
        """Load existing patterns from database."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('SELECT * FROM patterns')
            rows = cursor.fetchall()
            conn.close()
            
            for row in rows:
                pattern = PatternMemory(
                    pattern_id=row[0],
                    pattern_type=row[1],
                    frequency=row[2],
                    confidence=row[3],
                    examples=json.loads(row[4]),
                    reward_trend=json.loads(row[5]),
                    last_observed=row[6],
                    utility_score=row[7]
                )
                self.pattern_cache[pattern.pattern_id] = pattern
                
        except Exception as e:
            print(f"Error loading patterns: {e}")
    
    def get_memory_summary(self) -> Dict[str, Any]:
        """Get summary statistics of the memory system."""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Count by type
            cursor.execute('SELECT memory_type, COUNT(*) FROM memory_entries GROUP BY memory_type')
            type_counts = dict(cursor.fetchall())
            
            # Total memories
            cursor.execute('SELECT COUNT(*) FROM memory_entries')
            total_memories = cursor.fetchone()[0]
            
            # Average importance
            cursor.execute('SELECT AVG(importance) FROM memory_entries')
            avg_importance = cursor.fetchone()[0] or 0.0
            
            conn.close()
            
            return {
                'total_memories': total_memories,
                'type_counts': type_counts,
                'average_importance': avg_importance,
                'pattern_count': len(self.pattern_cache),
                'cache_sizes': {
                    'conversation': len(self.conversation_cache),
                    'insight': len(self.insight_cache),
                    'pattern': len(self.pattern_cache)
                }
            }
            
        except Exception as e:
            print(f"Error getting memory summary: {e}")
            return {}
    
    def cleanup_old_memories(self, max_age_days: int = 30):
        """Remove old, low-importance memories to save space."""
        cutoff_time = time.time() - (max_age_days * 24 * 3600)
        
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                DELETE FROM memory_entries 
                WHERE timestamp < ? AND importance < 0.3
            ''', (cutoff_time,))
            
            deleted_count = cursor.rowcount
            conn.commit()
            conn.close()
            
            print(f"Cleaned up {deleted_count} old, low-importance memories")
            
        except Exception as e:
            print(f"Error cleaning up old memories: {e}")
