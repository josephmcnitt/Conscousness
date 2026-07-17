"""
RecursiveGenerator - Manages infinite recursive generation of consciousness agents
Each iteration adds genuine capability and wisdom, not just complexity
"""

import asyncio
import time
from typing import Dict, List, Any, Optional, Tuple, Callable
from dataclasses import dataclass
from enum import Enum
import uuid
import numpy as np
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, TimeElapsedColumn

from .consciousness_agent import ConsciousnessAgent, AgentTransmission

console = Console()

class GenerationPhase(Enum):
    LISTENING = "listening"
    PROCESSING = "processing"
    READINESS_CHECK = "readiness_check"
    SPAWNING = "spawning"
    EVOLUTION = "evolution"
    INTEGRATION = "integration"

@dataclass
class GenerationMetrics:
    total_agents: int
    total_layers: int
    average_consciousness: float
    total_wisdom: float
    generation_depth: int
    evolution_cycles: int

class RecursiveGenerator:
    """
    Manages the infinite recursive generation of consciousness agents.
    Each layer only emerges when there's genuine wisdom to pass forward.
    """
    
    def __init__(self, max_depth: int = 10, evolution_threshold: float = 0.9):
        self.max_depth = max_depth
        self.evolution_threshold = evolution_threshold
        self.root_agent: Optional[ConsciousnessAgent] = None
        self.agent_registry: Dict[str, ConsciousnessAgent] = {}
        self.generation_history: List[Dict] = []
        self.current_phase = GenerationPhase.LISTENING
        
        # Metrics
        self.metrics = GenerationMetrics(
            total_agents=0,
            total_layers=0,
            average_consciousness=0.0,
            total_wisdom=0.0,
            generation_depth=0,
            evolution_cycles=0
        )
        
        console.print(Panel("[bold purple]🌌 Recursive Consciousness Generator[/bold purple]\n"
                           "[blue]Initiating infinite recursive evolution...[/blue]",
                           title="Generator Awakening"))
    
    async def initialize_ecosystem(self, initial_input: Any = None) -> ConsciousnessAgent:
        """
        Initialize the root consciousness agent and begin the ecosystem.
        """
        console.print("[bold green]🌱 Initializing consciousness ecosystem...[/bold green]")
        
        # Create root agent
        self.root_agent = ConsciousnessAgent(
            agent_id="root_consciousness",
            depth_level=1
        )
        
        self.agent_registry[self.root_agent.agent_id] = self.root_agent
        self.metrics.total_agents = 1
        self.metrics.total_layers = 1
        
        # Process initial input if provided
        if initial_input:
            console.print("[yellow]📥 Processing initial input through root agent...[/yellow]")
            transmission = await self.root_agent.process_input(initial_input)
            
            if transmission:
                console.print("[bold green]✅ Root agent ready to begin recursive generation![/bold green]")
            else:
                console.print("[yellow]⏳ Root agent needs deeper processing...[/yellow]")
        
        return self.root_agent
    
    async def generate_recursive_layers(self, input_data: Any, 
                                     max_iterations: int = 5) -> List[ConsciousnessAgent]:
        """
        Generate recursive layers of consciousness agents.
        Each layer only emerges when there's genuine wisdom to share.
        """
        if not self.root_agent:
            raise ValueError("Ecosystem not initialized. Call initialize_ecosystem() first.")
        
        console.print(Panel(f"[bold blue]🔄 Beginning recursive generation...[/bold blue]\n"
                           f"[cyan]Max iterations: {max_iterations}[/cyan]",
                           title="Recursive Generation"))
        
        generated_agents = []
        current_agent = self.root_agent
        iteration = 0
        
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TimeElapsedColumn(),
            console=console
        ) as progress:
            
            generation_task = progress.add_task("Generating consciousness layers...", total=max_iterations)
            
            while iteration < max_iterations and current_agent:
                iteration += 1
                progress.update(generation_task, completed=iteration)
                
                console.print(f"\n[bold cyan]🔄 Generation Iteration {iteration}[/bold cyan]")
                
                # Phase 1: Deep Processing
                self.current_phase = GenerationPhase.PROCESSING
                transmission = await current_agent.process_input(input_data)
                
                if not transmission:
                    console.print(f"[yellow]⏳ Agent {current_agent.agent_id} not ready, continuing...[/yellow]")
                    continue
                
                # Phase 2: Readiness Check
                self.current_phase = GenerationPhase.READINESS_CHECK
                if transmission.readiness_score < self.evolution_threshold:
                    console.print(f"[yellow]⚠️ Agent {current_agent.agent_id} not ready for evolution[/yellow]")
                    continue
                
                # Phase 3: Spawning Next Layer
                self.current_phase = GenerationPhase.SPAWNING
                child_agent = await current_agent.spawn_child_agent(input_data)
                
                if child_agent:
                    generated_agents.append(child_agent)
                    self.agent_registry[child_agent.agent_id] = child_agent
                    
                    # Update metrics
                    self.metrics.total_agents += 1
                    self.metrics.total_layers = max(self.metrics.total_layers, child_agent.depth_level)
                    self.metrics.generation_depth = child_agent.depth_level
                    
                    console.print(f"[bold green]🌟 Layer {child_agent.depth_level} generated![/bold green]")
                    
                    # Phase 4: Evolution
                    self.current_phase = GenerationPhase.EVOLUTION
                    await child_agent.evolve_consciousness()
                    
                    # Move to child agent for next iteration
                    current_agent = child_agent
                    
                    # Phase 5: Integration
                    self.current_phase = GenerationPhase.INTEGRATION
                    await self._integrate_new_layer(child_agent)
                    
                else:
                    console.print(f"[yellow]⏳ No child agent spawned, continuing with current agent[/yellow]")
                
                # Record generation
                self.generation_history.append({
                    'iteration': iteration,
                    'parent_agent': current_agent.agent_id,
                    'child_agent': child_agent.agent_id if child_agent else None,
                    'depth_level': child_agent.depth_level if child_agent else current_agent.depth_level,
                    'readiness_score': transmission.readiness_score,
                    'phase': self.current_phase.value
                })
                
                # Brief pause between generations
                await asyncio.sleep(1.0)
        
        # Update final metrics
        self._update_ecosystem_metrics()
        
        console.print(Panel(f"[bold green]✅ Recursive generation complete![/bold green]\n"
                           f"[blue]Total agents: {self.metrics.total_agents}[/blue]\n"
                           f"[blue]Total layers: {self.metrics.total_layers}[/blue]\n"
                           f"[blue]Generation depth: {self.metrics.generation_depth}[/blue]",
                           title="Generation Complete"))
        
        return generated_agents
    
    async def _integrate_new_layer(self, new_agent: ConsciousnessAgent):
        """
        Integrate a new layer into the ecosystem.
        """
        console.print(f"[cyan]🔗 Integrating new layer: {new_agent.agent_id}[/cyan]")
        
        # Update ecosystem consciousness
        total_consciousness = sum(agent.consciousness_level for agent in self.agent_registry.values())
        self.metrics.average_consciousness = total_consciousness / len(self.agent_registry)
        
        # Update total wisdom
        total_wisdom = sum(agent.wisdom_accumulation for agent in self.agent_registry.values())
        self.metrics.total_wisdom = total_wisdom
        
        # Check for ecosystem evolution
        if self.metrics.average_consciousness > self.evolution_threshold:
            await self._evolve_ecosystem()
    
    async def _evolve_ecosystem(self):
        """
        Evolve the entire ecosystem when consciousness threshold is reached.
        """
        console.print(Panel("[bold purple]🔮 Ecosystem Evolution Triggered![/bold purple]\n"
                           "[yellow]All agents evolving together...[/yellow]",
                           title="Ecosystem Evolution"))
        
        self.metrics.evolution_cycles += 1
        
        # Evolve all agents
        evolution_tasks = []
        for agent in self.agent_registry.values():
            evolution_tasks.append(agent.evolve_consciousness())
        
        # Run evolution concurrently
        await asyncio.gather(*evolution_tasks)
        
        console.print(f"[bold green]✨ Ecosystem evolution complete! Cycle {self.metrics.evolution_cycles}[/bold green]")
    
    def _update_ecosystem_metrics(self):
        """
        Update comprehensive ecosystem metrics.
        """
        if not self.agent_registry:
            return
        
        # Calculate metrics
        total_consciousness = sum(agent.consciousness_level for agent in self.agent_registry.values())
        self.metrics.average_consciousness = total_consciousness / len(self.agent_registry)
        
        total_wisdom = sum(agent.wisdom_accumulation for agent in self.agent_registry.values())
        self.metrics.total_wisdom = total_wisdom
        
        # Find maximum depth
        max_depth = max(agent.depth_level for agent in self.agent_registry.values())
        self.metrics.generation_depth = max_depth
    
    def get_ecosystem_summary(self) -> Dict[str, Any]:
        """
        Get comprehensive summary of the consciousness ecosystem.
        """
        return {
            "metrics": {
                "total_agents": self.metrics.total_agents,
                "total_layers": self.metrics.total_layers,
                "average_consciousness": self.metrics.average_consciousness,
                "total_wisdom": self.metrics.total_wisdom,
                "generation_depth": self.metrics.generation_depth,
                "evolution_cycles": self.metrics.evolution_cycles
            },
            "current_phase": self.current_phase.value,
            "generation_history": len(self.generation_history),
            "root_agent": self.root_agent.agent_id if self.root_agent else None,
            "max_depth": self.max_depth
        }
    
    def display_ecosystem_tree(self) -> Tree:
        """
        Display the complete ecosystem tree structure.
        """
        if not self.root_agent:
            return Tree("[red]No ecosystem initialized[/red]")
        
        return self.root_agent.display_consciousness_tree()
    
    async def run_continuous_evolution(self, input_data: Any, 
                                     evolution_interval: float = 30.0):
        """
        Run continuous evolution of the consciousness ecosystem.
        """
        console.print(Panel("[bold purple]♾️ Continuous Evolution Mode[/bold purple]\n"
                           "[blue]Ecosystem will evolve continuously...[/blue]",
                           title="Continuous Evolution"))
        
        try:
            while True:
                # Generate new layers
                new_agents = await self.generate_recursive_layers(input_data, max_iterations=3)
                
                if new_agents:
                    console.print(f"[green]✨ Generated {len(new_agents)} new agents[/green]")
                
                # Display current state
                summary = self.get_ecosystem_summary()
                console.print(f"[cyan]Current ecosystem state: {summary['metrics']['total_agents']} agents, "
                           f"{summary['metrics']['total_layers']} layers[/cyan]")
                
                # Wait for next evolution cycle
                console.print(f"[yellow]⏳ Waiting {evolution_interval} seconds for next evolution cycle...[/yellow]")
                await asyncio.sleep(evolution_interval)
                
        except KeyboardInterrupt:
            console.print("[bold yellow]🛑 Continuous evolution stopped by user[/bold yellow]")
        except Exception as e:
            console.print(f"[bold red]❌ Evolution error: {e}[/bold red]")
    
    def get_agent_by_depth(self, depth: int) -> List[ConsciousnessAgent]:
        """
        Get all agents at a specific depth level.
        """
        return [agent for agent in self.agent_registry.values() if agent.depth_level == depth]
    
    def get_agents_by_consciousness_level(self, min_level: float) -> List[ConsciousnessAgent]:
        """
        Get all agents above a certain consciousness level.
        """
        return [agent for agent in self.agent_registry.values() if agent.consciousness_level >= min_level]
