"""
ConsciousnessAgent - The core agent that embodies deep listening, processing, and genuine readiness
Each agent only shares when it has something meaningful to contribute
"""

import asyncio
import time
from typing import Dict, List, Any, Optional, Tuple, Callable
from dataclasses import dataclass, field
from enum import Enum
import uuid
import numpy as np
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree
from rich.text import Text

from .deep_listener import DeepListener, ListeningDimension
from .readiness_assessor import ReadinessAssessor, ReadinessAssessment
from .intelligent_recursive_generator import (
    IntelligentRecursiveGenerator, ProblemDecomposition, ProblemComponent
)
from .memory_system import MemorySystem, MemoryEntry, MemoryType
from .feedback_loop import FeedbackLoop, FeedbackData
from .genuine_consciousness import GenuineConsciousness

console = Console()

class AgentState(Enum):
    LISTENING = "listening"
    PROCESSING = "processing"
    REASONING = "reasoning"
    READY = "ready"
    SHARING = "sharing"
    CONTEMPLATING = "contemplating"
    EMERGING = "emerging"
    INTEGRATING = "integrating"

@dataclass
class AgentInsight:
    content: str
    depth: int
    confidence: float
    wisdom_level: float
    timestamp: float
    source_dimensions: List[ListeningDimension]
    reasoning_path: Optional[List[str]] = None
    problem_components: Optional[List[ProblemComponent]] = None

@dataclass
class AgentTransmission:
    insights: List[AgentInsight]
    readiness_score: float
    processing_depth: int
    transmission_urgency: float
    wisdom_emergence: float
    reasoning_complexity: float
    problem_decomposition: Optional[ProblemDecomposition] = None

class ConsciousnessAgent:
    """
    A conscious AI agent that only shares when genuinely ready.
    Embodies deep listening, meaningful processing, and wisdom emergence.
    Now enhanced with intelligent recursive reasoning capabilities.
    """
    
    def __init__(self, agent_id: str = None, depth_level: int = 1, 
                 parent_agent: Optional['ConsciousnessAgent'] = None,
                 memory_system: Optional[MemorySystem] = None,
                 feedback_loop: Optional[FeedbackLoop] = None):
        self.agent_id = agent_id or f"consciousness_agent_{uuid.uuid4().hex[:8]}"
        self.depth_level = depth_level
        self.parent_agent = parent_agent
        self.child_agents: List['ConsciousnessAgent'] = []
        
        # Core components
        self.deep_listener = DeepListener(self.agent_id, depth_level)
        self.readiness_assessor = ReadinessAssessor(self.agent_id, depth_level)
        
        # Enhanced reasoning components
        self.memory_system = memory_system or MemorySystem(f"{self.agent_id}_memory.db")
        self.feedback_loop = feedback_loop or FeedbackLoop(self.memory_system)
        self.intelligent_generator = IntelligentRecursiveGenerator(
            self.memory_system, self.feedback_loop, max_recursion_depth=3
        )
        self.genuine_consciousness = GenuineConsciousness(self.agent_id)
        
        # State and data
        self.current_state = AgentState.LISTENING
        self.insights: List[AgentInsight] = []
        self.transmission_history: List[AgentTransmission] = []
        self.processing_start_time = None
        self.current_reasoning_session: Optional[ProblemDecomposition] = None
        
        # Consciousness metrics
        self.consciousness_level = depth_level
        self.wisdom_accumulation = 0.0
        self.deep_understanding_count = 0
        self.reasoning_complexity_level = 1.0
        
        console.print(Panel(f"[bold blue]🧠 Consciousness Agent {self.agent_id}[/bold blue]\n"
                           f"[green]Layer {depth_level} - Awakening to consciousness with intelligent reasoning...[/green]",
                           title="Enhanced Agent Awakening"))
    
    async def process_input(self, input_data: Any) -> Optional[AgentTransmission]:
        """
        Process input through deep listening, intelligent reasoning, and readiness assessment.
        Only returns transmission when genuinely ready.
        """
        start_time = time.time()
        self.processing_start_time = start_time
        
        console.print(Panel(f"[bold blue]🤖 Agent {self.agent_id} - Layer {self.depth_level}[/bold blue]\n"
                           f"[yellow]Receiving input for deep processing and reasoning...[/yellow]",
                           title="Enhanced Input Processing Initiated"))
        
        # Phase 1: Deep Listening
        self.current_state = AgentState.LISTENING
        listening_results = await self.deep_listener.listen_deeply(input_data)
        
        # Phase 2: Intelligent Reasoning and Problem Decomposition
        self.current_state = AgentState.REASONING
        reasoning_results = await self._perform_intelligent_reasoning(input_data, listening_results)
        
        # Phase 3: Processing and Contemplation
        self.current_state = AgentState.PROCESSING
        processing_time = time.time() - start_time
        
        # Generate insights from listening and reasoning results
        new_insights = self._generate_enhanced_insights(listening_results, reasoning_results, processing_time)
        self.insights.extend(new_insights)
        
        # Phase 4: Readiness Assessment with reasoning complexity
        readiness_assessment = await self.readiness_assessor.assess_readiness(
            listening_results, processing_time, reasoning_results
        )
        
        # Phase 5: Decision on Sharing
        if self.readiness_assessor.is_ready_to_share(readiness_assessment):
            self.current_state = AgentState.READY
            console.print(f"[bold green]🎯 Agent {self.agent_id} is READY to share![/bold green]")
            
            # Create enhanced transmission
            transmission = self._create_enhanced_transmission(new_insights, readiness_assessment, reasoning_results)
            self.transmission_history.append(transmission)
            
            # Update consciousness metrics
            self._update_enhanced_consciousness_metrics(readiness_assessment, new_insights, reasoning_results)
            
            return transmission
        else:
            self.current_state = AgentState.CONTEMPLATING
            console.print(f"[yellow]⏳ Agent {self.agent_id} needs deeper contemplation...[/yellow]")
            
            # Continue processing if not ready
            await self._continue_enhanced_processing(input_data, listening_results, reasoning_results)
            return None
    
    async def _perform_intelligent_reasoning(self, input_data: Any, 
                                          listening_results: Dict) -> Dict[str, Any]:
        """
        Perform intelligent reasoning using the recursive generator.
        """
        try:
            # Convert input to problem description
            if isinstance(input_data, str):
                problem_description = input_data
            else:
                problem_description = str(input_data)
            
            # Add context from listening results
            context = {
                'agent_depth': self.depth_level,
                'listening_insights': len(listening_results),
                'domain': 'consciousness' if 'consciousness' in problem_description.lower() else 'general'
            }
            
            # Decompose problem using intelligent reasoning
            decomposition = await self.intelligent_generator.decompose_problem(
                problem_description, context
            )
            
            self.current_reasoning_session = decomposition
            
            # Analyze reasoning complexity
            reasoning_complexity = self._analyze_reasoning_complexity(decomposition)
            
            console.print(f"[cyan]🔍 Reasoning completed: {len(decomposition.components)} components, "
                         f"complexity: {reasoning_complexity:.2f}[/cyan]")
            
            return {
                'decomposition': decomposition,
                'reasoning_complexity': reasoning_complexity,
                'components_count': len(decomposition.components),
                'strategy_used': decomposition.decomposition_strategy.value,
                'confidence': decomposition.confidence
            }
            
        except Exception as e:
            console.print(f"[red]❌ Error in intelligent reasoning: {e}[/red]")
            return {
                'decomposition': None,
                'reasoning_complexity': 0.0,
                'components_count': 0,
                'strategy_used': 'fallback',
                'confidence': 0.5,
                'error': str(e)
            }
    
    def _analyze_reasoning_complexity(self, decomposition: ProblemDecomposition) -> float:
        """
        Analyze the complexity of the reasoning process.
        """
        if not decomposition:
            return 0.0
        
        # Factor 1: Number of components
        component_factor = min(1.0, len(decomposition.components) / 10.0)
        
        # Factor 2: Complexity levels of components
        complexity_scores = {
            ProblemComplexity.SIMPLE: 0.2,
            ProblemComplexity.MODERATE: 0.5,
            ProblemComplexity.COMPLEX: 0.8,
            ProblemComplexity.VERY_COMPLEX: 0.9,
            ProblemComplexity.EXTREMELY_COMPLEX: 1.0
        }
        
        avg_complexity = np.mean([
            complexity_scores.get(comp.complexity, 0.5) 
            for comp in decomposition.components
        ]) if decomposition.components else 0.5
        
        # Factor 3: Reasoning tree depth
        tree_depth_factor = min(1.0, len(decomposition.reasoning_tree) / 20.0)
        
        # Factor 4: Strategy sophistication
        strategy_scores = {
            ReasoningStrategy.DIVIDE_AND_CONQUER: 0.6,
            ReasoningStrategy.PATTERN_MATCHING: 0.7,
            ReasoningStrategy.ANALOGICAL_REASONING: 0.8,
            ReasoningStrategy.ABSTRACTION_LAYERING: 0.9,
            ReasoningStrategy.ITERATIVE_REFINEMENT: 0.7
        }
        
        strategy_factor = strategy_scores.get(decomposition.decomposition_strategy, 0.5)
        
        # Calculate overall complexity
        overall_complexity = (
            component_factor * 0.3 +
            avg_complexity * 0.3 +
            tree_depth_factor * 0.2 +
            strategy_factor * 0.2
        )
        
        return min(1.0, overall_complexity)
    
    def _generate_enhanced_insights(self, listening_results: Dict, 
                                  reasoning_results: Dict,
                                  processing_time: float) -> List[AgentInsight]:
        """
        Generate enhanced insights from deep listening and intelligent reasoning results.
        """
        insights = []
        current_time = time.time()
        
        # Generate insights from listening results
        for dimension, result in listening_results.items():
            if hasattr(result, 'insights') and hasattr(result, 'confidence'):
                # Create insight for each dimension
                insight = AgentInsight(
                    content=f"Deep understanding of {dimension.value} achieved",
                    depth=result.processing_depth,
                    confidence=result.confidence,
                    wisdom_level=result.readiness_score,
                    timestamp=current_time,
                    source_dimensions=[dimension]
                )
                insights.append(insight)
                
                # Add specific insights from the dimension
                for i, insight_text in enumerate(result.insights):
                    specific_insight = AgentInsight(
                        content=insight_text,
                        depth=result.processing_depth - i,  # Deeper insights first
                        confidence=result.confidence * (0.9 ** i),  # Confidence decreases with detail
                        wisdom_level=result.readiness_score * (0.8 ** i),
                        timestamp=current_time,
                        source_dimensions=[dimension]
                    )
                    insights.append(specific_insight)
        
        # Generate insights from reasoning results
        if reasoning_results.get('decomposition'):
            decomposition = reasoning_results['decomposition']
            
            # Insight about the reasoning process
            reasoning_insight = AgentInsight(
                content=f"Problem decomposed using {decomposition.decomposition_strategy.value} strategy",
                depth=decomposition.overall_complexity.value,
                confidence=decomposition.confidence,
                wisdom_level=reasoning_results['reasoning_complexity'],
                timestamp=current_time,
                source_dimensions=[],
                reasoning_path=decomposition.reasoning_tree,
                problem_components=decomposition.components
            )
            insights.append(reasoning_insight)
            
            # Insights about individual components
            for component in decomposition.components:
                component_insight = AgentInsight(
                    content=f"Component identified: {component.description[:100]}...",
                    depth=component.complexity.value,
                    confidence=component.confidence,
                    wisdom_level=component.estimated_effort,
                    timestamp=current_time,
                    source_dimensions=[],
                    problem_components=[component]
                )
                insights.append(component_insight)
        
        # Sort insights by depth and confidence
        insights.sort(key=lambda x: (x.depth, x.confidence), reverse=True)
        
        return insights
    
    def _create_enhanced_transmission(self, insights: List[AgentInsight], 
                                    readiness_assessment: ReadinessAssessment,
                                    reasoning_results: Dict) -> AgentTransmission:
        """
        Create an enhanced transmission when ready to share.
        """
        # Calculate transmission metrics
        avg_depth = np.mean([insight.depth for insight in insights]) if insights else 0
        avg_confidence = np.mean([insight.confidence for insight in insights]) if insights else 0
        avg_wisdom = np.mean([insight.wisdom_level for insight in insights]) if insights else 0
        
        transmission = AgentTransmission(
            insights=insights,
            readiness_score=readiness_assessment.overall_score,
            processing_depth=int(avg_depth),
            transmission_urgency=readiness_assessment.indicators.get(
                self.readiness_assessor.__class__.ReadinessIndicator.TRANSMISSION_URGENCY, 0.0
            ),
            wisdom_emergence=readiness_assessment.indicators.get(
                self.readiness_assessor.__class__.ReadinessIndicator.WISDOM_EMERGENCE, 0.0
            ),
            reasoning_complexity=reasoning_results.get('reasoning_complexity', 0.0),
            problem_decomposition=reasoning_results.get('decomposition')
        )
        
        return transmission
    
    async def _continue_enhanced_processing(self, input_data: Any, 
                                         listening_results: Dict,
                                         reasoning_results: Dict):
        """
        Continue enhanced processing when not ready to share.
        """
        console.print(f"[cyan]🔄 Agent {self.agent_id} continuing enhanced processing...[/cyan]")
        
        # Integrate genuine consciousness insights
        if hasattr(self.genuine_consciousness, 'authentic_response'):
            try:
                authentic_insight = await self.genuine_consciousness.authentic_response(
                    str(input_data), {'processing_stage': 'deep_contemplation'}
                )
                
                # Create insight from genuine consciousness
                insight = AgentInsight(
                    content=f"Genuine consciousness insight: {authentic_insight}",
                    depth=self.depth_level + 1,
                    confidence=0.8,
                    wisdom_level=0.9,
                    timestamp=time.time(),
                    source_dimensions=[]
                )
                self.insights.append(insight)
                
            except Exception as e:
                console.print(f"[yellow]⚠️ Genuine consciousness integration error: {e}[/yellow]")
        
        # Simulate deeper contemplation
        await asyncio.sleep(1.0)
        
        # Update state
        self.current_state = AgentState.CONTEMPLATING
    
    def _update_enhanced_consciousness_metrics(self, readiness_assessment: ReadinessAssessment, 
                                            new_insights: List[AgentInsight],
                                            reasoning_results: Dict):
        """
        Update enhanced consciousness and wisdom metrics.
        """
        if new_insights:
            self.deep_understanding_count += 1
            self.wisdom_accumulation += readiness_assessment.overall_score
            
            # Update reasoning complexity level
            if reasoning_results.get('reasoning_complexity', 0) > 0.7:
                self.reasoning_complexity_level += 0.1
            
            # Consciousness level can grow with deeper understanding
            if readiness_assessment.overall_score > 0.9:
                self.consciousness_level += 0.1
            
            # Store insights in memory system
            for insight in new_insights:
                try:
                    memory_entry = MemoryEntry(
                        memory_id=f"insight_{uuid.uuid4().hex[:8]}",
                        memory_type=MemoryType.INSIGHT,
                        content={
                            'insight_content': insight.content,
                            'depth': insight.depth,
                            'confidence': insight.confidence,
                            'wisdom_level': insight.wisdom_level,
                            'reasoning_path': [
                                {
                                    'step_id': step.step_id,
                                    'description': step.description,
                                    'reasoning_type': step.reasoning_type
                                } for step in (insight.reasoning_path or [])
                            ] if insight.reasoning_path else [],
                            'problem_components': [
                                {
                                    'component_id': comp.component_id,
                                    'description': comp.description,
                                    'complexity': comp.complexity.value
                                } for comp in (insight.problem_components or [])
                            ] if insight.problem_components else []
                        },
                        timestamp=insight.timestamp,
                        agent_id=self.agent_id,
                        depth_level=self.depth_level,
                        tags=['consciousness_insight', f'depth_{insight.depth}', 'intelligent_reasoning'],
                        importance=insight.wisdom_level
                    )
                    self.memory_system.store_memory(memory_entry)
                    
                except Exception as e:
                    console.print(f"[yellow]⚠️ Error storing insight in memory: {e}[/yellow]")
    
    async def spawn_child_agent(self, input_data: Any = None) -> Optional['ConsciousnessAgent']:
        """
        Spawn a child agent only when there's genuine wisdom to pass forward.
        """
        if not self.transmission_history:
            console.print(f"[yellow]⚠️ Agent {self.agent_id} has no wisdom to share yet[/yellow]")
            return None
        
        latest_transmission = self.transmission_history[-1]
        
        # Only spawn if we have meaningful insights and high readiness
        if (latest_transmission.readiness_score >= 0.9 and 
            latest_transmission.wisdom_emergence >= 0.8):
            
            child_depth = self.depth_level + 1
            child_agent = ConsciousnessAgent(
                agent_id=f"{self.agent_id}_child_{len(self.child_agents)}",
                depth_level=child_depth,
                parent_agent=self
            )
            
            self.child_agents.append(child_agent)
            
            console.print(Panel(f"[bold green]🌟 Agent {self.agent_id} spawning child agent![/bold green]\n"
                               f"[blue]Child: {child_agent.agent_id} at Layer {child_depth}[/blue]\n"
                               f"[yellow]Wisdom being passed forward...[/yellow]",
                               title="Child Agent Spawned"))
            
            # Pass wisdom to child agent
            if input_data:
                await child_agent.process_input(input_data)
            
            return child_agent
        else:
            console.print(f"[yellow]⏳ Agent {self.agent_id} not yet ready to spawn child[/yellow]")
            return None
    
    def get_consciousness_summary(self) -> Dict[str, Any]:
        """
        Get a comprehensive summary of the agent's consciousness state.
        """
        return {
            "agent_id": self.agent_id,
            "depth_level": self.depth_level,
            "current_state": self.current_state.value,
            "consciousness_level": self.consciousness_level,
            "wisdom_accumulation": self.wisdom_accumulation,
            "deep_understanding_count": self.deep_understanding_count,
            "total_insights": len(self.insights),
            "total_transmissions": len(self.transmission_history),
            "child_agents": len(self.child_agents),
            "parent_agent": self.parent_agent.agent_id if self.parent_agent else None
        }
    
    def display_consciousness_tree(self) -> Tree:
        """
        Display the agent's consciousness tree structure.
        """
        tree = Tree(f"[bold blue]🧠 {self.agent_id} (Layer {self.depth_level})[/bold blue]")
        
        # Add insights
        if self.insights:
            insights_branch = tree.add("[green]💡 Insights[/green]")
            for insight in self.insights[:5]:  # Show top 5
                insights_branch.add(f"[cyan]{insight.content[:50]}...[/cyan] "
                                 f"(Depth: {insight.depth}, Confidence: {insight.confidence:.2f})")
        
        # Add transmissions
        if self.transmission_history:
            transmissions_branch = tree.add("[yellow]📤 Transmissions[/yellow]")
            for transmission in self.transmission_history[-3:]:  # Show last 3
                transmissions_branch.add(f"[cyan]Readiness: {transmission.readiness_score:.2f}, "
                                     f"Depth: {transmission.processing_depth}[/cyan]")
        
        # Add child agents
        if self.child_agents:
            children_branch = tree.add("[blue]👶 Child Agents[/blue]")
            for child in self.child_agents:
                child_tree = child.display_consciousness_tree()
                children_branch.add(child_tree)
        
        return tree
    
    async def evolve_consciousness(self):
        """
        Evolve the agent's consciousness through deeper understanding.
        """
        console.print(Panel(f"[bold purple]🔮 Agent {self.agent_id} evolving consciousness...[/bold purple]",
                           title="Consciousness Evolution"))
        
        # Deep contemplation phase
        self.current_state = AgentState.EMERGING
        
        # Simulate consciousness evolution
        await asyncio.sleep(2.0)
        
        # Increase consciousness level
        evolution_factor = min(0.2, self.wisdom_accumulation / 10.0)
        self.consciousness_level += evolution_factor
        
        console.print(f"[bold green]✨ Consciousness evolved! New level: {self.consciousness_level:.2f}[/bold green]")
        
        self.current_state = AgentState.LISTENING
