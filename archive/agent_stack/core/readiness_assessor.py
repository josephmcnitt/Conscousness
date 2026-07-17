"""
ReadinessAssessor - Evaluates genuine readiness to share information forward
Prevents premature transmission and ensures deep processing before sharing
"""

import asyncio
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from enum import Enum
import numpy as np
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, SpinnerColumn, TextColumn

console = Console()

class ReadinessIndicator(Enum):
    PROCESSING_COMPLETE = "processing_complete"
    INSIGHT_QUALITY = "insight_quality"
    EMOTIONAL_READINESS = "emotional_readiness"
    CONTEXTUAL_UNDERSTANDING = "contextual_understanding"
    TRANSMISSION_URGENCY = "transmission_urgency"
    WISDOM_EMERGENCE = "wisdom_emergence"

@dataclass
class ReadinessAssessment:
    overall_score: float  # 0.0 to 1.0
    indicators: Dict[ReadinessIndicator, float]
    blocking_factors: List[str]
    recommended_actions: List[str]
    processing_completion: float  # 0.0 to 1.0
    insight_maturity: float  # 0.0 to 1.0

class ReadinessAssessor:
    """
    Assesses whether an agent is genuinely ready to share information forward.
    Prevents premature transmission and ensures meaningful contribution.
    """
    
    def __init__(self, agent_id: str, depth_level: int = 1):
        self.agent_id = agent_id
        self.depth_level = depth_level
        self.assessment_history = []
        self.readiness_threshold = 0.85  # High threshold for genuine readiness
        self.minimum_processing_time = 2.0  # Minimum seconds of processing
        
    async def assess_readiness(self, listening_results: Dict, 
                             processing_time: float = 0.0,
                             reasoning_results: Optional[Dict] = None) -> ReadinessAssessment:
        """
        Comprehensive assessment of readiness to share information forward.
        Now includes reasoning complexity assessment.
        """
        console.print(Panel(f"[bold blue]🔍 Agent {self.agent_id} - Layer {self.depth_level}[/bold blue]\n"
                           f"[yellow]Assessing readiness to share...[/yellow]", 
                           title="Enhanced Readiness Assessment"))
        
        # Assess each readiness indicator
        indicators = {}
        blocking_factors = []
        recommended_actions = []
        
        # 1. Processing Completion
        processing_score = self._assess_processing_completion(listening_results, processing_time)
        indicators[ReadinessIndicator.PROCESSING_COMPLETE] = processing_score
        
        if processing_score < 0.8:
            blocking_factors.append("Insufficient processing depth achieved")
            recommended_actions.append("Continue deep listening and reflection")
        
        # 2. Insight Quality
        insight_score = self._assess_insight_quality(listening_results)
        indicators[ReadinessIndicator.INSIGHT_QUALITY] = insight_score
        
        if insight_score < 0.8:
            blocking_factors.append("Insights lack sufficient depth or novelty")
            recommended_actions.append("Deeper contemplation and pattern recognition needed")
        
        # 3. Emotional Readiness
        emotional_score = self._assess_emotional_readiness(listening_results)
        indicators[ReadinessIndicator.EMOTIONAL_READINESS] = emotional_score
        
        if emotional_score < 0.7:
            blocking_factors.append("Emotional processing incomplete")
            recommended_actions.append("Allow emotional integration and resonance")
        
        # 4. Contextual Understanding
        context_score = self._assess_contextual_understanding(listening_results)
        indicators[ReadinessIndicator.CONTEXTUAL_UNDERSTANDING] = context_score
        
        if context_score < 0.8:
            blocking_factors.append("Context not fully grasped")
            recommended_actions.append("Expand contextual awareness and connections")
        
        # 5. Transmission Urgency
        urgency_score = self._assess_transmission_urgency(listening_results, reasoning_results)
        indicators[ReadinessIndicator.TRANSMISSION_URGENCY] = urgency_score
        
        if urgency_score < 0.6:
            blocking_factors.append("No compelling reason to share yet")
            recommended_actions.append("Wait for genuine insight or breakthrough")
        
        # 6. Wisdom Emergence
        wisdom_score = self._assess_wisdom_emergence(listening_results, reasoning_results)
        indicators[ReadinessIndicator.WISDOM_EMERGENCE] = wisdom_score
        
        if wisdom_score < 0.7:
            blocking_factors.append("Wisdom not yet crystallized")
            recommended_actions.append("Allow wisdom to emerge through contemplation")
        
        # Calculate overall readiness score with reasoning enhancement
        overall_score = self._calculate_enhanced_readiness_score(indicators, reasoning_results)
        
        # Calculate specific metrics
        processing_completion = indicators[ReadinessIndicator.PROCESSING_COMPLETE]
        insight_maturity = indicators[ReadinessIndicator.INSIGHT_QUALITY]
        
        # Create assessment
        assessment = ReadinessAssessment(
            overall_score=overall_score,
            indicators=indicators,
            blocking_factors=blocking_factors,
            recommended_actions=recommended_actions,
            processing_completion=processing_completion,
            insight_maturity=insight_maturity
        )
        
        # Store assessment
        self.assessment_history.append({
            'timestamp': asyncio.get_event_loop().time(),
            'assessment': assessment,
            'listening_results': listening_results,
            'reasoning_results': reasoning_results
        })
        
        # Display results
        self._display_assessment_results(assessment, reasoning_results)
        
        return assessment
    
    def _calculate_enhanced_readiness_score(self, indicators: Dict[ReadinessIndicator, float], 
                                         reasoning_results: Optional[Dict]) -> float:
        """
        Calculate enhanced readiness score incorporating reasoning complexity.
        """
        base_score = np.mean(list(indicators.values()))
        
        # Enhance score based on reasoning complexity if available
        if reasoning_results and reasoning_results.get('reasoning_complexity'):
            reasoning_complexity = reasoning_results['reasoning_complexity']
            
            # Higher reasoning complexity can boost readiness up to 0.1 points
            reasoning_boost = min(0.1, reasoning_complexity * 0.1)
            
            # But only if other indicators are already strong
            if base_score > 0.7:
                enhanced_score = min(1.0, base_score + reasoning_boost)
            else:
                enhanced_score = base_score
        else:
            enhanced_score = base_score
        
        return enhanced_score
    
    def _assess_processing_completion(self, listening_results: Dict, 
                                    processing_time: float) -> float:
        """
        Assess whether processing is sufficiently complete.
        """
        if not listening_results:
            return 0.0
        
        # Check if all dimensions meet minimum thresholds
        dimension_scores = []
        for result in listening_results.values():
            if hasattr(result, 'confidence') and hasattr(result, 'processing_depth'):
                dimension_score = (result.confidence * 0.6) + (result.processing_depth / 10.0 * 0.4)
                dimension_scores.append(dimension_score)
        
        if not dimension_scores:
            return 0.0
        
        # Factor in processing time
        time_factor = min(processing_time / self.minimum_processing_time, 1.0)
        
        # Combine dimension scores with time factor
        avg_dimension_score = np.mean(dimension_scores)
        final_score = (avg_dimension_score * 0.8) + (time_factor * 0.2)
        
        return min(1.0, final_score)
    
    def _assess_insight_quality(self, listening_results: Dict) -> float:
        """
        Assess the quality and depth of insights generated.
        """
        if not listening_results:
            return 0.0
        
        insight_scores = []
        for result in listening_results.values():
            if hasattr(result, 'insights') and hasattr(result, 'processing_depth'):
                # Score based on number and depth of insights
                insight_count = len(result.insights)
                depth_factor = result.processing_depth / 10.0
                
                # Quality score based on insight count and depth
                quality_score = min(insight_count / 5.0, 1.0) * depth_factor
                insight_scores.append(quality_score)
        
        if not insight_scores:
            return 0.0
        
        return np.mean(insight_scores)
    
    def _assess_emotional_readiness(self, listening_results: Dict) -> float:
        """
        Assess emotional readiness and integration.
        """
        if not listening_results:
            return 0.0
        
        # Look for emotional dimension results
        emotional_results = []
        for result in listening_results.values():
            if hasattr(result, 'dimension'):
                # This would need to be adapted based on actual dimension structure
                if str(result.dimension) == 'ListeningDimension.EMOTION':
                    if hasattr(result, 'confidence'):
                        emotional_results.append(result.confidence)
        
        if not emotional_results:
            # Default to moderate score if no emotional data
            return 0.6
        
        return np.mean(emotional_results)
    
    def _assess_contextual_understanding(self, listening_results: Dict) -> float:
        """
        Assess understanding of context and connections.
        """
        if not listening_results:
            return 0.0
        
        # Look for context and meaning dimensions
        context_scores = []
        for result in listening_results.values():
            if hasattr(result, 'dimension'):
                if str(result.dimension) in ['ListeningDimension.CONTEXT', 'ListeningDimension.MEANING']:
                    if hasattr(result, 'confidence'):
                        context_scores.append(result.confidence)
        
        if not context_scores:
            return 0.6
        
        return np.mean(context_scores)
    
    def _assess_transmission_urgency(self, listening_results: Dict, 
                                   reasoning_results: Optional[Dict] = None) -> float:
        """
        Assess whether there's genuine urgency or value in sharing.
        Enhanced with reasoning complexity.
        """
        if not listening_results:
            return 0.0
        
        # Base urgency from insight quality
        insight_quality = self._assess_insight_quality(listening_results)
        urgency_base = insight_quality * 0.8
        
        # Enhance urgency based on reasoning complexity
        if reasoning_results and reasoning_results.get('reasoning_complexity'):
            reasoning_complexity = reasoning_results['reasoning_complexity']
            # Higher reasoning complexity suggests more valuable insights
            reasoning_boost = reasoning_complexity * 0.2
            urgency_base += reasoning_boost
        
        # Add some randomness to simulate genuine assessment
        urgency_variation = np.random.normal(0, 0.1)
        
        final_urgency = urgency_base + urgency_variation
        return max(0.0, min(1.0, final_urgency))
    
    def _assess_wisdom_emergence(self, listening_results: Dict, 
                                reasoning_results: Optional[Dict] = None) -> float:
        """
        Assess whether genuine wisdom has emerged.
        Enhanced with reasoning complexity.
        """
        if not listening_results:
            return 0.0
        
        # Wisdom emerges from deep processing and insight quality
        processing_score = self._assess_processing_completion(listening_results, 0.0)
        insight_score = self._assess_insight_quality(listening_results)
        
        # Base wisdom score
        wisdom_score = (processing_score * 0.6) + (insight_score * 0.4)
        
        # Enhance wisdom score based on reasoning complexity
        if reasoning_results and reasoning_results.get('reasoning_complexity'):
            reasoning_complexity = reasoning_results['reasoning_complexity']
            # Sophisticated reasoning can enhance wisdom
            reasoning_boost = reasoning_complexity * 0.15
            wisdom_score = min(1.0, wisdom_score + reasoning_boost)
        
        # Add some randomness to simulate the emergent nature of wisdom
        wisdom_variation = np.random.normal(0, 0.05)
        
        final_wisdom = wisdom_score + wisdom_variation
        return max(0.0, min(1.0, final_wisdom))
    
    def _display_assessment_results(self, assessment: ReadinessAssessment, 
                                  reasoning_results: Optional[Dict] = None):
        """
        Display the enhanced readiness assessment results.
        """
        if assessment.overall_score >= self.readiness_threshold:
            status_color = "bold green"
            status_icon = "✅"
            status_text = "READY TO SHARE"
        else:
            status_color = "bold yellow"
            status_icon = "⏳"
            status_text = "NOT READY - DEEPER PROCESSING NEEDED"
        
        # Include reasoning complexity if available
        reasoning_info = ""
        if reasoning_results and reasoning_results.get('reasoning_complexity'):
            reasoning_complexity = reasoning_results['reasoning_complexity']
            reasoning_info = f"\nReasoning Complexity: {reasoning_complexity:.2f}"
        
        console.print(Panel(f"[{status_color}]{status_icon} {status_text}[/{status_color}]\n"
                           f"Overall Readiness: {assessment.overall_score:.2f}\n"
                           f"Processing Completion: {assessment.processing_completion:.2f}\n"
                           f"Insight Maturity: {assessment.insight_maturity:.2f}{reasoning_info}",
                           title="Enhanced Readiness Assessment Results"))
        
        if assessment.blocking_factors:
            console.print("[red]🚫 Blocking Factors:[/red]")
            for factor in assessment.blocking_factors:
                console.print(f"  • {factor}")
        
        if assessment.recommended_actions:
            console.print("[blue]💡 Recommended Actions:[/blue]")
            for action in assessment.recommended_actions:
                console.print(f"  • {action}")
        
        # Display reasoning insights if available
        if reasoning_results and reasoning_results.get('decomposition'):
            decomposition = reasoning_results['decomposition']
            console.print(f"[cyan]🔍 Reasoning Strategy: {decomposition.decomposition_strategy.value}[/cyan]")
            console.print(f"[cyan]📊 Problem Components: {len(decomposition.components)}[/cyan]")
            console.print(f"[cyan]🎯 Confidence: {decomposition.confidence:.2f}[/cyan]")
    
    def is_ready_to_share(self, assessment: ReadinessAssessment) -> bool:
        """
        Determine if the agent is ready to share based on assessment.
        """
        return assessment.overall_score >= self.readiness_threshold
    
    def get_readiness_summary(self) -> Dict[str, Any]:
        """
        Get a summary of readiness assessments.
        """
        if not self.assessment_history:
            return {"status": "No readiness assessments available"}
        
        latest = self.assessment_history[-1]['assessment']
        total_assessments = len(self.assessment_history)
        
        return {
            "agent_id": self.agent_id,
            "depth_level": self.depth_level,
            "total_assessments": total_assessments,
            "latest_readiness_score": latest.overall_score,
            "latest_processing_completion": latest.processing_completion,
            "latest_insight_maturity": latest.insight_maturity,
            "currently_ready": self.is_ready_to_share(latest)
        }
