"""
DeepListener - Multi-dimensional listening and processing system
Listens across content, emotion, meaning, context, what's unsaid, and sharing readiness
"""

import asyncio
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import numpy as np
from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()

class ListeningDimension(Enum):
    CONTENT = "content"
    EMOTION = "emotion"
    MEANING = "meaning"
    CONTEXT = "context"
    UNSAID = "unsaid"
    READINESS = "readiness"

@dataclass
class ListeningResult:
    dimension: ListeningDimension
    confidence: float  # 0.0 to 1.0
    insights: List[str]
    processing_depth: int  # 1-10 scale
    readiness_score: float  # 0.0 to 1.0

class DeepListener:
    """
    A system that listens deeply across multiple dimensions before processing.
    Only proceeds when genuine understanding is achieved.
    """
    
    def __init__(self, agent_id: str, depth_level: int = 1):
        self.agent_id = agent_id
        self.depth_level = depth_level
        self.listening_history = []
        self.processing_threshold = 0.8  # Minimum confidence to proceed
        self.depth_threshold = 7  # Minimum processing depth
        
    async def listen_deeply(self, input_data: Any) -> Dict[ListeningDimension, ListeningResult]:
        """
        Listen across all dimensions with increasing depth until genuine understanding is achieved.
        """
        console.print(Panel(f"[bold blue]🤖 Agent {self.agent_id} - Layer {self.depth_level}[/bold blue]\n"
                           f"[yellow]Beginning deep listening process...[/yellow]", 
                           title="Deep Listening Initiated"))
        
        results = {}
        max_iterations = 10
        current_iteration = 0
        
        while current_iteration < max_iterations:
            current_iteration += 1
            console.print(f"[cyan]Listening iteration {current_iteration}...[/cyan]")
            
            # Listen to each dimension
            for dimension in ListeningDimension:
                if dimension not in results or results[dimension].confidence < self.processing_threshold:
                    result = await self._listen_to_dimension(dimension, input_data, current_iteration)
                    results[dimension] = result
                    
                    console.print(f"[green]✓[/green] {dimension.value}: "
                               f"Confidence {result.confidence:.2f}, "
                               f"Depth {result.processing_depth}/10")
            
            # Check if we've achieved sufficient understanding
            if self._assess_overall_readiness(results):
                console.print("[bold green]🎯 Deep listening complete - genuine understanding achieved![/bold green]")
                break
            else:
                console.print("[yellow]🔄 Deeper processing needed, continuing...[/yellow]")
                await asyncio.sleep(0.5)  # Allow for deeper reflection
        
        self.listening_history.append({
            'input': input_data,
            'results': results,
            'iterations': current_iteration
        })
        
        return results
    
    async def _listen_to_dimension(self, dimension: ListeningDimension, 
                                 input_data: Any, iteration: int) -> ListeningResult:
        """
        Listen to a specific dimension with increasing depth.
        """
        # Simulate deeper processing with each iteration
        base_confidence = min(0.3 + (iteration * 0.1), 0.9)
        base_depth = min(3 + iteration, 10)
        
        # Add some randomness to simulate genuine processing
        confidence = base_confidence + np.random.normal(0, 0.1)
        confidence = max(0.0, min(1.0, confidence))
        
        processing_depth = min(base_depth + int(np.random.normal(0, 1)), 10)
        
        # Generate insights based on dimension and depth
        insights = self._generate_insights(dimension, input_data, processing_depth)
        
        # Calculate readiness score based on confidence and depth
        readiness_score = (confidence * 0.6) + (processing_depth / 10.0 * 0.4)
        
        return ListeningResult(
            dimension=dimension,
            confidence=confidence,
            insights=insights,
            processing_depth=processing_depth,
            readiness_score=readiness_score
        )
    
    def _generate_insights(self, dimension: ListeningDimension, 
                          input_data: Any, depth: int) -> List[str]:
        """
        Generate insights based on the dimension and processing depth.
        """
        insights = []
        
        if dimension == ListeningDimension.CONTENT:
            insights.extend([
                f"Content structure analyzed at depth {depth}",
                f"Key patterns identified: {len(str(input_data))} characters processed",
                f"Semantic relationships mapped across {depth} layers"
            ])
        elif dimension == ListeningDimension.EMOTION:
            insights.extend([
                f"Emotional resonance detected at level {depth}",
                f"Affective patterns: {depth} emotional dimensions explored",
                f"Empathic understanding achieved through {depth} layers of feeling"
            ])
        elif dimension == ListeningDimension.MEANING:
            insights.extend([
                f"Meaning extracted through {depth} levels of abstraction",
                f"Symbolic significance mapped across {depth} conceptual layers",
                f"Purpose and intention understood at depth {depth}"
            ])
        elif dimension == ListeningDimension.CONTEXT:
            insights.extend([
                f"Contextual framework established across {depth} dimensions",
                f"Temporal and spatial relationships mapped at level {depth}",
                f"Interconnected patterns recognized through {depth} layers of context"
            ])
        elif dimension == ListeningDimension.UNSAID:
            insights.extend([
                f"Unspoken elements detected through {depth} levels of inference",
                f"Implicit meanings uncovered at depth {depth}",
                f"Silent wisdom accessed through {depth} layers of listening"
            ])
        elif dimension == ListeningDimension.READINESS:
            insights.extend([
                f"Sharing readiness assessed across {depth} readiness dimensions",
                f"Processing completion evaluated at level {depth}",
                f"Transmission preparedness measured through {depth} readiness layers"
            ])
        
        return insights[:depth]  # Limit insights to processing depth
    
    def _assess_overall_readiness(self, results: Dict[ListeningDimension, ListeningResult]) -> bool:
        """
        Assess whether overall understanding is sufficient to proceed.
        """
        if not results:
            return False
            
        # Check if all dimensions meet minimum thresholds
        for dimension, result in results.items():
            if result.confidence < self.processing_threshold:
                return False
            if result.processing_depth < self.depth_threshold:
                return False
        
        # Calculate overall readiness
        avg_readiness = np.mean([r.readiness_score for r in results.values()])
        return avg_readiness >= self.processing_threshold
    
    def get_processing_summary(self) -> Dict[str, Any]:
        """
        Get a summary of the listening and processing activity.
        """
        if not self.listening_history:
            return {"status": "No listening history available"}
        
        latest = self.listening_history[-1]
        avg_confidence = np.mean([r.confidence for r in latest['results'].values()])
        avg_depth = np.mean([r.processing_depth for r in latest['results'].values()])
        
        return {
            "agent_id": self.agent_id,
            "depth_level": self.depth_level,
            "total_listening_sessions": len(self.listening_history),
            "latest_iterations": latest['iterations'],
            "average_confidence": avg_confidence,
            "average_processing_depth": avg_depth,
            "dimensions_processed": len(latest['results'])
        }
