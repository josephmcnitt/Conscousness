"""
FeedbackLoop - Self-improving system that learns from rewards and adjusts agent strategies
Enables continuous improvement of reasoning, communication, and consciousness evolution
"""

import time
import json
import hashlib
from typing import Dict, List, Any, Optional, Tuple, Callable
from dataclasses import dataclass, field
from enum import Enum
import numpy as np
from collections import defaultdict, deque
import uuid

from .reward_system import RewardEvaluator, RewardScores, RewardDimensions
from .memory_system import MemorySystem, MemoryEntry, MemoryType


class LearningStrategy(str, Enum):
    """Different strategies for learning from feedback."""
    REWARD_OPTIMIZATION = "reward_optimization"
    PATTERN_RECOGNITION = "pattern_recognition"
    STRATEGY_ADAPTATION = "strategy_adaptation"
    META_LEARNING = "meta_learning"


@dataclass
class FeedbackData:
    """Data structure for storing feedback information."""
    feedback_id: str
    agent_id: str
    depth_level: int
    input_data: Any
    response: str
    reward_scores: RewardScores
    context: Dict[str, Any]
    timestamp: float
    learning_insights: List[str] = field(default_factory=list)
    strategy_adjustments: Dict[str, Any] = field(default_factory=dict)


@dataclass
class LearningOutcome:
    """Outcome of learning from feedback."""
    strategy_improvements: Dict[str, float]
    new_patterns: List[str]
    confidence_gain: float
    adaptation_success: bool
    next_strategies: List[str]


class StrategyAdjustment:
    """Represents an adjustment to an agent's strategy."""
    
    def __init__(self, strategy_name: str, current_value: float, 
                 target_value: float, confidence: float):
        self.strategy_name = strategy_name
        self.current_value = current_value
        self.target_value = target_value
        self.confidence = confidence
        self.adjustment_magnitude = target_value - current_value
        self.implementation_priority = abs(self.adjustment_magnitude) * confidence


class FeedbackLoop:
    """
    Self-improving feedback loop that learns from rewards and adjusts strategies.
    Enables agents to continuously improve their reasoning and communication.
    """
    
    def __init__(self, memory_system: MemorySystem, 
                 learning_rate: float = 0.1,
                 adaptation_threshold: float = 0.7):
        self.memory_system = memory_system
        self.learning_rate = learning_rate
        self.adaptation_threshold = adaptation_threshold
        
        # Feedback tracking
        self.feedback_history: List[FeedbackData] = []
        self.strategy_performance: Dict[str, List[float]] = defaultdict(list)
        self.learning_patterns: Dict[str, Dict] = defaultdict(dict)
        
        # Strategy management
        self.active_strategies: Dict[str, Dict] = {}
        self.strategy_evolution: Dict[str, List[Dict]] = defaultdict(list)
        
        # Performance metrics
        self.overall_improvement_rate = 0.0
        self.strategy_success_rate = 0.0
        self.adaptation_frequency = 0.0
        
        # Initialize default strategies
        self._initialize_default_strategies()
    
    def _initialize_default_strategies(self):
        """Initialize default learning strategies."""
        self.active_strategies = {
            "response_length": {
                "current_value": 0.5,
                "target_value": 0.7,
                "confidence": 0.5,
                "adaptation_rate": 0.1
            },
            "complexity_level": {
                "current_value": 0.6,
                "target_value": 0.8,
                "confidence": 0.5,
                "adaptation_rate": 0.1
            },
            "creativity_boost": {
                "current_value": 0.4,
                "target_value": 0.6,
                "confidence": 0.5,
                "adaptation_rate": 0.1
            },
            "coherence_emphasis": {
                "current_value": 0.7,
                "target_value": 0.9,
                "confidence": 0.5,
                "adaptation_rate": 0.1
            }
        }
    
    def process_feedback(self, feedback_data: FeedbackData) -> LearningOutcome:
        """
        Process feedback and generate learning outcomes.
        This is the core of the self-improvement system.
        """
        # Store feedback in memory
        self._store_feedback(feedback_data)
        
        # Analyze reward patterns
        reward_analysis = self._analyze_reward_patterns(feedback_data)
        
        # Generate strategy adjustments
        strategy_adjustments = self._generate_strategy_adjustments(feedback_data, reward_analysis)
        
        # Apply learning and update strategies
        learning_insights = self._apply_learning(feedback_data, strategy_adjustments)
        
        # Update performance metrics
        self._update_performance_metrics(feedback_data, strategy_adjustments)
        
        # Generate next strategies
        next_strategies = self._generate_next_strategies(feedback_data, learning_insights)
        
        return LearningOutcome(
            strategy_improvements=strategy_adjustments,
            new_patterns=learning_insights,
            confidence_gain=reward_analysis.get('confidence_gain', 0.0),
            adaptation_success=len(strategy_adjustments) > 0,
            next_strategies=next_strategies
        )
    
    def _store_feedback(self, feedback_data: FeedbackData):
        """Store feedback data in the memory system."""
        # Create memory entry for the feedback
        memory_entry = MemoryEntry(
            memory_id=feedback_data.feedback_id,
            memory_type=MemoryType.LEARNING,
            content={
                'input_data': feedback_data.input_data,
                'response': feedback_data.response,
                'reward_scores': feedback_data.reward_scores.as_dict(),
                'context': feedback_data.context,
                'learning_insights': feedback_data.learning_insights,
                'strategy_adjustments': feedback_data.strategy_adjustments
            },
            timestamp=feedback_data.timestamp,
            agent_id=feedback_data.feedback_id,
            depth_level=feedback_data.depth_level,
            reward_scores=feedback_data.reward_scores,
            tags=['feedback', 'learning', f'depth_{feedback_data.depth_level}'],
            importance=feedback_data.reward_scores.overall()
        )
        
        self.memory_system.store_memory(memory_entry)
        self.feedback_history.append(feedback_data)
    
    def _analyze_reward_patterns(self, feedback_data: FeedbackData) -> Dict[str, Any]:
        """Analyze reward patterns to identify learning opportunities."""
        analysis = {
            'overall_score': feedback_data.reward_scores.overall(),
            'dimension_scores': feedback_data.reward_scores.as_dict(),
            'improvement_areas': [],
            'strengths': [],
            'confidence_gain': 0.0
        }
        
        # Identify areas for improvement
        for dimension, score in feedback_data.reward_scores.as_dict().items():
            if score < 0.6:
                analysis['improvement_areas'].append(dimension)
            elif score > 0.8:
                analysis['strengths'].append(dimension)
        
        # Calculate confidence gain based on consistency
        if len(self.feedback_history) > 1:
            recent_scores = [f.reward_scores.overall() for f in self.feedback_history[-5:]]
            analysis['confidence_gain'] = np.std(recent_scores) * -1  # Lower std = higher confidence
        
        return analysis
    
    def _generate_strategy_adjustments(self, feedback_data: FeedbackData, 
                                    reward_analysis: Dict[str, Any]) -> Dict[str, float]:
        """Generate strategy adjustments based on feedback analysis."""
        adjustments = {}
        
        # Adjust strategies based on reward scores
        for dimension, score in feedback_data.reward_scores.as_dict().items():
            if dimension in reward_analysis['improvement_areas']:
                # Increase emphasis on this dimension
                strategy_key = self._get_strategy_key_for_dimension(dimension)
                if strategy_key in self.active_strategies:
                    current_value = self.active_strategies[strategy_key]['current_value']
                    target_value = min(1.0, current_value + self.learning_rate)
                    adjustments[strategy_key] = target_value
        
        # Adjust response length based on efficiency score
        if feedback_data.reward_scores.efficiency < 0.6:
            if 'response_length' in self.active_strategies:
                current_length = self.active_strategies['response_length']['current_value']
                target_length = max(0.3, current_length - self.learning_rate)
                adjustments['response_length'] = target_length
        
        # Adjust complexity based on correctness and coherence
        if (feedback_data.reward_scores.correctness < 0.6 or 
            feedback_data.reward_scores.coherence < 0.6):
            if 'complexity_level' in self.active_strategies:
                current_complexity = self.active_strategies['complexity_level']['current_value']
                target_complexity = max(0.4, current_complexity - self.learning_rate)
                adjustments['complexity_level'] = target_complexity
        
        return adjustments
    
    def _get_strategy_key_for_dimension(self, dimension: str) -> str:
        """Map reward dimensions to strategy keys."""
        dimension_strategy_map = {
            RewardDimensions.CORRECTNESS: 'complexity_level',
            RewardDimensions.EFFICIENCY: 'response_length',
            RewardDimensions.CREATIVITY: 'creativity_boost',
            RewardDimensions.COHERENCE: 'coherence_emphasis'
        }
        return dimension_strategy_map.get(dimension, 'complexity_level')
    
    def _apply_learning(self, feedback_data: FeedbackData, 
                       strategy_adjustments: Dict[str, float]) -> List[str]:
        """Apply learning and update active strategies."""
        learning_insights = []
        
        # Apply strategy adjustments
        for strategy_key, new_value in strategy_adjustments.items():
            if strategy_key in self.active_strategies:
                old_value = self.active_strategies[strategy_key]['current_value']
                self.active_strategies[strategy_key]['current_value'] = new_value
                
                # Record the evolution
                evolution_record = {
                    'timestamp': time.time(),
                    'old_value': old_value,
                    'new_value': new_value,
                    'trigger': f"feedback_{feedback_data.feedback_id}",
                    'reward_improvement': feedback_data.reward_scores.overall()
                }
                self.strategy_evolution[strategy_key].append(evolution_record)
                
                learning_insights.append(f"Adjusted {strategy_key}: {old_value:.3f} → {new_value:.3f}")
        
        # Update strategy confidence based on performance
        for strategy_key in self.active_strategies:
            if strategy_key in strategy_adjustments:
                # Increase confidence when we make adjustments
                current_confidence = self.active_strategies[strategy_key]['confidence']
                new_confidence = min(0.95, current_confidence + self.learning_rate * 0.5)
                self.active_strategies[strategy_key]['confidence'] = new_confidence
                
                learning_insights.append(f"Increased confidence in {strategy_key}: {current_confidence:.3f} → {new_confidence:.3f}")
        
        return learning_insights
    
    def _update_performance_metrics(self, feedback_data: FeedbackData, 
                                  strategy_adjustments: Dict[str, float]):
        """Update performance metrics based on feedback."""
        # Update overall improvement rate
        if len(self.feedback_history) > 1:
            recent_scores = [f.reward_scores.overall() for f in self.feedback_history[-10:]]
            if len(recent_scores) >= 2:
                improvement_rate = (recent_scores[-1] - recent_scores[0]) / len(recent_scores)
                self.overall_improvement_rate = (
                    self.overall_improvement_rate * 0.9 + improvement_rate * 0.1
                )
        
        # Update strategy success rate
        if strategy_adjustments:
            self.strategy_success_rate = (
                self.strategy_success_rate * 0.9 + 1.0 * 0.1
            )
        else:
            self.strategy_success_rate = (
                self.strategy_success_rate * 0.9 + 0.0 * 0.1
            )
        
        # Update adaptation frequency
        self.adaptation_frequency = (
            self.adaptation_frequency * 0.9 + (1.0 if strategy_adjustments else 0.0) * 0.1
        )
    
    def _generate_next_strategies(self, feedback_data: FeedbackData, 
                                learning_insights: List[str]) -> List[str]:
        """Generate next strategies based on learning insights."""
        next_strategies = []
        
        # Analyze patterns in learning insights
        if 'response_length' in learning_insights:
            next_strategies.append("optimize_response_length")
        
        if 'complexity_level' in learning_insights:
            next_strategies.append("adjust_complexity_dynamically")
        
        if 'creativity_boost' in learning_insights:
            next_strategies.append("enhance_creative_expression")
        
        if 'coherence_emphasis' in learning_insights:
            next_strategies.append("improve_logical_flow")
        
        # Add meta-learning strategies
        if len(learning_insights) > 3:
            next_strategies.append("meta_learning_optimization")
        
        return next_strategies
    
    def get_current_strategies(self) -> Dict[str, Any]:
        """Get current active strategies and their states."""
        return {
            'strategies': self.active_strategies.copy(),
            'performance_metrics': {
                'overall_improvement_rate': self.overall_improvement_rate,
                'strategy_success_rate': self.strategy_success_rate,
                'adaptation_frequency': self.adaptation_frequency
            },
            'recent_evolution': {
                strategy: evolution[-5:] if evolution else []
                for strategy, evolution in self.strategy_evolution.items()
            }
        }
    
    def get_learning_summary(self) -> Dict[str, Any]:
        """Get comprehensive learning summary."""
        return {
            'total_feedback_processed': len(self.feedback_history),
            'strategy_count': len(self.active_strategies),
            'performance_metrics': {
                'overall_improvement_rate': self.overall_improvement_rate,
                'strategy_success_rate': self.strategy_success_rate,
                'adaptation_frequency': self.adaptation_frequency
            },
            'active_strategies': self.active_strategies,
            'recent_feedback': [
                {
                    'agent_id': f.agent_id,
                    'overall_score': f.reward_scores.overall(),
                    'timestamp': f.timestamp
                }
                for f in self.feedback_history[-10:]
            ] if self.feedback_history else []
        }
    
    def reset_strategies(self):
        """Reset all strategies to default values."""
        self._initialize_default_strategies()
        self.strategy_evolution.clear()
        self.overall_improvement_rate = 0.0
        self.strategy_success_rate = 0.0
        self.adaptation_frequency = 0.0
        print("Strategies reset to default values")
    
    def export_learning_data(self, filepath: str) -> bool:
        """Export learning data to JSON file."""
        try:
            export_data = {
                'timestamp': time.time(),
                'learning_summary': self.get_learning_summary(),
                'strategy_evolution': dict(self.strategy_evolution),
                'feedback_history': [
                    {
                        'feedback_id': f.feedback_id,
                        'agent_id': f.agent_id,
                        'overall_score': f.reward_scores.overall(),
                        'timestamp': f.timestamp,
                        'learning_insights': f.learning_insights
                    }
                    for f in self.feedback_history
                ]
            }
            
            with open(filepath, 'w') as f:
                json.dump(export_data, f, indent=2, default=str)
            
            return True
            
        except Exception as e:
            print(f"Error exporting learning data: {e}")
            return False
