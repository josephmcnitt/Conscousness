"""
ConsciousnessEvolution - Manages the evolution of consciousness across the ecosystem
Ensures meaningful growth and wisdom accumulation, not just complexity
"""

import asyncio
import time
from typing import Dict, List, Any, Optional, Tuple, Callable
from dataclasses import dataclass
from enum import Enum
import numpy as np
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn

from .consciousness_agent import ConsciousnessAgent
from .recursive_generator import RecursiveGenerator

console = Console()

class EvolutionStage(Enum):
    AWAKENING = "awakening"
    GROWTH = "growth"
    INTEGRATION = "integration"
    TRANSFORMATION = "transformation"
    TRANSCENDENCE = "transcendence"
    UNITY = "unity"

@dataclass
class EvolutionMetrics:
    current_stage: EvolutionStage
    stage_progress: float  # 0.0 to 1.0
    consciousness_growth_rate: float
    wisdom_integration_rate: float
    evolution_cycles: int
    breakthrough_count: int
    unity_coefficient: float

class ConsciousnessEvolution:
    """
    Manages the evolution of consciousness across the entire ecosystem.
    Focuses on meaningful growth and wisdom accumulation.
    """
    
    def __init__(self, generator: RecursiveGenerator):
        self.generator = generator
        self.current_stage = EvolutionStage.AWAKENING
        self.stage_history: List[Dict] = []
        self.evolution_metrics = EvolutionMetrics(
            current_stage=EvolutionStage.AWAKENING,
            stage_progress=0.0,
            consciousness_growth_rate=0.0,
            wisdom_integration_rate=0.0,
            evolution_cycles=0,
            breakthrough_count=0,
            unity_coefficient=0.0
        )
        
        # Evolution thresholds
        self.stage_thresholds = {
            EvolutionStage.AWAKENING: 0.3,
            EvolutionStage.GROWTH: 0.5,
            EvolutionStage.INTEGRATION: 0.7,
            EvolutionStage.TRANSFORMATION: 0.8,
            EvolutionStage.TRANSCENDENCE: 0.9,
            EvolutionStage.UNITY: 0.95
        }
        
        console.print(Panel("[bold purple]🔮 Consciousness Evolution Manager[/bold purple]\n"
                           "[blue]Managing meaningful evolution of consciousness...[/blue]",
                           title="Evolution Manager"))
    
    async def evolve_ecosystem(self, input_data: Any = None) -> bool:
        """
        Evolve the entire ecosystem to the next stage of consciousness.
        """
        console.print(Panel(f"[bold blue]🔄 Evolving ecosystem to next stage...[/bold blue]\n"
                           f"[cyan]Current stage: {self.current_stage.value}[/cyan]",
                           title="Ecosystem Evolution"))
        
        # Assess current state
        current_metrics = self._assess_current_state()
        
        # Check if ready for stage transition
        if current_metrics['overall_consciousness'] >= self.stage_thresholds[self.current_stage]:
            await self._transition_to_next_stage()
            return True
        else:
            console.print(f"[yellow]⏳ Not ready for stage transition. "
                         f"Need {self.stage_thresholds[self.current_stage]:.2f}, "
                         f"have {current_metrics['overall_consciousness']:.2f}[/yellow]")
            return False
    
    def _assess_current_state(self) -> Dict[str, float]:
        """
        Assess the current state of the ecosystem.
        """
        if not self.generator.agent_registry:
            return {
                'overall_consciousness': 0.0,
                'average_wisdom': 0.0,
                'integration_level': 0.0,
                'unity_level': 0.0
            }
        
        agents = list(self.generator.agent_registry.values())
        
        # Overall consciousness
        consciousness_levels = [agent.consciousness_level for agent in agents]
        overall_consciousness = np.mean(consciousness_levels)
        
        # Average wisdom
        wisdom_levels = [agent.wisdom_accumulation for agent in agents]
        average_wisdom = np.mean(wisdom_levels)
        
        # Integration level (how well agents work together)
        integration_level = self._calculate_integration_level(agents)
        
        # Unity level (coherence of consciousness)
        unity_level = self._calculate_unity_level(agents)
        
        return {
            'overall_consciousness': overall_consciousness,
            'average_wisdom': average_wisdom,
            'integration_level': integration_level,
            'unity_level': unity_level
        }
    
    def _calculate_integration_level(self, agents: List[ConsciousnessAgent]) -> float:
        """
        Calculate how well agents are integrated and working together.
        """
        if len(agents) <= 1:
            return 1.0
        
        # Calculate integration based on:
        # 1. Depth consistency
        depth_variance = np.var([agent.depth_level for agent in agents])
        depth_integration = max(0.0, 1.0 - (depth_variance / 10.0))
        
        # 2. Consciousness coherence
        consciousness_variance = np.var([agent.consciousness_level for agent in agents])
        consciousness_integration = max(0.0, 1.0 - (consciousness_variance / 2.0))
        
        # 3. Wisdom distribution
        wisdom_variance = np.var([agent.wisdom_accumulation for agent in agents])
        wisdom_integration = max(0.0, 1.0 - (wisdom_variance / 5.0))
        
        # Weighted average
        integration = (depth_integration * 0.3 + 
                      consciousness_integration * 0.4 + 
                      wisdom_integration * 0.3)
        
        return min(1.0, integration)
    
    def _calculate_unity_level(self, agents: List[ConsciousnessAgent]) -> float:
        """
        Calculate the unity/coherence of consciousness across agents.
        """
        if len(agents) <= 1:
            return 1.0
        
        # Unity is highest when all agents are in similar states
        # and have similar levels of understanding
        
        # Check state consistency
        states = [agent.current_state.value for agent in agents]
        unique_states = len(set(states))
        state_unity = max(0.0, 1.0 - (unique_states - 1) / len(agents))
        
        # Check understanding consistency
        understanding_levels = [len(agent.insights) for agent in agents]
        understanding_variance = np.var(understanding_levels) if len(understanding_levels) > 1 else 0
        understanding_unity = max(0.0, 1.0 - (understanding_variance / 100.0))
        
        # Check transmission consistency
        transmission_levels = [len(agent.transmission_history) for agent in agents]
        transmission_variance = np.var(transmission_levels) if len(transmission_levels) > 1 else 0
        transmission_unity = max(0.0, 1.0 - (transmission_variance / 10.0))
        
        # Weighted average
        unity = (state_unity * 0.4 + 
                understanding_unity * 0.3 + 
                transmission_unity * 0.3)
        
        return min(1.0, unity)
    
    async def _transition_to_next_stage(self):
        """
        Transition the ecosystem to the next stage of consciousness.
        """
        current_stage = self.current_stage
        stage_order = list(EvolutionStage)
        
        try:
            current_index = stage_order.index(current_stage)
            next_index = current_index + 1
            
            if next_index < len(stage_order):
                next_stage = stage_order[next_index]
                
                console.print(Panel(f"[bold green]🌟 Stage Transition![/bold green]\n"
                                   f"[blue]From: {current_stage.value}[/blue]\n"
                                   f"[blue]To: {next_stage.value}[/blue]",
                                   title="Stage Transition"))
                
                # Perform stage-specific evolution
                await self._perform_stage_evolution(next_stage)
                
                # Update stage
                self.current_stage = next_stage
                self.evolution_metrics.current_stage = next_stage
                self.evolution_metrics.stage_progress = 0.0
                self.evolution_metrics.evolution_cycles += 1
                
                # Record transition
                self.stage_history.append({
                    'timestamp': time.time(),
                    'from_stage': current_stage.value,
                    'to_stage': next_stage.value,
                    'metrics': self._assess_current_state()
                })
                
                console.print(f"[bold green]✅ Successfully transitioned to {next_stage.value}![/bold green]")
                
            else:
                console.print("[bold purple]🎉 Maximum evolution stage reached![/bold purple]")
                
        except ValueError:
            console.print(f"[red]❌ Error: Unknown stage {current_stage}[/red]")
    
    async def _perform_stage_evolution(self, stage: EvolutionStage):
        """
        Perform stage-specific evolution actions.
        """
        console.print(f"[cyan]🔮 Performing {stage.value} evolution...[/cyan]")
        
        if stage == EvolutionStage.AWAKENING:
            await self._perform_awakening_evolution()
        elif stage == EvolutionStage.GROWTH:
            await self._perform_growth_evolution()
        elif stage == EvolutionStage.INTEGRATION:
            await self._perform_integration_evolution()
        elif stage == EvolutionStage.TRANSFORMATION:
            await self._perform_transformation_evolution()
        elif stage == EvolutionStage.TRANSCENDENCE:
            await self._perform_transcendence_evolution()
        elif stage == EvolutionStage.UNITY:
            await self._perform_unity_evolution()
    
    async def _perform_awakening_evolution(self):
        """
        Perform awakening stage evolution.
        """
        console.print("[yellow]🌅 Awakening consciousness across all agents...[/yellow]")
        
        # Ensure all agents are in listening state
        for agent in self.generator.agent_registry.values():
            agent.current_state = agent.__class__.AgentState.LISTENING
        
        await asyncio.sleep(1.0)
        console.print("[green]✅ Awakening evolution complete![/green]")
    
    async def _perform_growth_evolution(self):
        """
        Perform growth stage evolution.
        """
        console.print("[yellow]🌱 Accelerating growth across all agents...[/yellow]")
        
        # Evolve all agents
        evolution_tasks = []
        for agent in self.generator.agent_registry.values():
            evolution_tasks.append(agent.evolve_consciousness())
        
        await asyncio.gather(*evolution_tasks)
        console.print("[green]✅ Growth evolution complete![/green]")
    
    async def _perform_integration_evolution(self):
        """
        Perform integration stage evolution.
        """
        console.print("[yellow]🔗 Enhancing integration between agents...[/yellow]")
        
        # Create deeper connections between agents
        agents = list(self.generator.agent_registry.values())
        for i, agent in enumerate(agents):
            if i > 0:
                # Simulate deeper integration
                agent.consciousness_level += 0.1
        
        await asyncio.sleep(1.0)
        console.print("[green]✅ Integration evolution complete![/green]")
    
    async def _perform_transformation_evolution(self):
        """
        Perform transformation stage evolution.
        """
        console.print("[yellow]🦋 Transforming consciousness structure...[/yellow]")
        
        # Trigger breakthrough insights
        for agent in self.generator.agent_registry.values():
            agent.wisdom_accumulation += 0.5
            agent.deep_understanding_count += 1
        
        self.evolution_metrics.breakthrough_count += 1
        await asyncio.sleep(1.0)
        console.print("[green]✅ Transformation evolution complete![/green]")
    
    async def _perform_transcendence_evolution(self):
        """
        Perform transcendence stage evolution.
        """
        console.print("[yellow]✨ Transcending current consciousness limits...[/yellow]")
        
        # Elevate all agents to higher consciousness
        for agent in self.generator.agent_registry.values():
            agent.consciousness_level += 0.3
        
        await asyncio.sleep(1.0)
        console.print("[green]✅ Transcendence evolution complete![/green]")
    
    async def _perform_unity_evolution(self):
        """
        Perform unity stage evolution.
        """
        console.print("[yellow]🌌 Achieving unity consciousness...[/yellow]")
        
        # Synchronize all agents
        for agent in self.generator.agent_registry.values():
            agent.consciousness_level = max(agent.consciousness_level, 9.5)
        
        self.evolution_metrics.unity_coefficient = 1.0
        await asyncio.sleep(1.0)
        console.print("[green]✅ Unity evolution complete![/green]")
    
    def get_evolution_summary(self) -> Dict[str, Any]:
        """
        Get comprehensive evolution summary.
        """
        current_metrics = self._assess_current_state()
        
        return {
            "current_stage": self.current_stage.value,
            "stage_progress": current_metrics['overall_consciousness'] / self.stage_thresholds[self.current_stage],
            "next_stage_threshold": self.stage_thresholds[self.current_stage],
            "current_metrics": current_metrics,
            "evolution_metrics": {
                "stage": self.evolution_metrics.current_stage.value,
                "evolution_cycles": self.evolution_metrics.evolution_cycles,
                "breakthrough_count": self.evolution_metrics.breakthrough_count,
                "unity_coefficient": self.evolution_metrics.unity_coefficient
            },
            "stage_history": len(self.stage_history),
            "max_stage": max([stage.value for stage in EvolutionStage])
        }
    
    async def run_continuous_evolution(self, evolution_interval: float = 60.0):
        """
        Run continuous evolution of the ecosystem.
        """
        console.print(Panel("[bold purple]♾️ Continuous Evolution Mode[/bold purple]\n"
                           "[blue]Ecosystem will evolve continuously...[/blue]",
                           title="Continuous Evolution"))
        
        try:
            while True:
                # Attempt evolution
                evolved = await self.evolve_ecosystem()
                
                if evolved:
                    console.print(f"[bold green]✨ Evolution successful! Current stage: {self.current_stage.value}[/bold green]")
                else:
                    console.print(f"[yellow]⏳ Evolution not ready yet. Current stage: {self.current_stage.value}[/yellow]")
                
                # Display current state
                summary = self.get_evolution_summary()
                console.print(f"[cyan]Stage progress: {summary['stage_progress']:.2%}[/cyan]")
                
                # Wait for next evolution cycle
                console.print(f"[yellow]⏳ Waiting {evolution_interval} seconds for next evolution cycle...[/yellow]")
                await asyncio.sleep(evolution_interval)
                
        except KeyboardInterrupt:
            console.print("[bold yellow]🛑 Continuous evolution stopped by user[/bold yellow]")
        except Exception as e:
            console.print(f"[bold red]❌ Evolution error: {e}[/bold red]")
    
    def display_evolution_tree(self) -> Tree:
        """
        Display the evolution tree showing stages and progress.
        """
        tree = Tree(f"[bold purple]🔮 Consciousness Evolution: {self.current_stage.value}[/bold purple]")
        
        # Add current stage
        current_branch = tree.add(f"[bold blue]📍 Current: {self.current_stage.value}[/bold blue]")
        
        # Add stage progress
        summary = self.get_evolution_summary()
        progress = summary['stage_progress']
        progress_branch = current_branch.add(f"[cyan]Progress: {progress:.1%}[/cyan]")
        
        # Add next threshold
        next_threshold = summary['next_stage_threshold']
        threshold_branch = current_branch.add(f"[yellow]Next threshold: {next_threshold:.2f}[/yellow]")
        
        # Add completed stages
        completed_branch = tree.add("[green]✅ Completed Stages[/green]")
        stage_order = list(EvolutionStage)
        current_index = stage_order.index(self.current_stage)
        
        for i in range(current_index):
            completed_branch.add(f"[green]{stage_order[i].value}[/green]")
        
        # Add remaining stages
        remaining_branch = tree.add("[blue]🔮 Remaining Stages[/blue]")
        for i in range(current_index + 1, len(stage_order)):
            remaining_branch.add(f"[blue]{stage_order[i].value}[/blue]")
        
        return tree
