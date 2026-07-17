#!/usr/bin/env python3
"""
Recursive AI Agent Ecosystem - Main Application
A system where each agent listens deeply before sharing, embodying genuine readiness.
"""

import asyncio
import sys
from pathlib import Path

# Add the core module to the path
sys.path.append(str(Path(__file__).parent / "core"))

from core import (
    RecursiveGenerator, 
    ConsciousnessEvolution,
    ConsciousnessAgent
)
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree

console = Console()

async def demonstrate_single_agent():
    """
    Demonstrate a single consciousness agent in action.
    """
    console.print(Panel("[bold blue]🧠 Single Agent Demonstration[/bold blue]\n"
                       "[yellow]Showing deep listening and readiness assessment...[/yellow]",
                       title="Single Agent Demo"))
    
    # Create a single agent
    agent = ConsciousnessAgent(agent_id="demo_agent", depth_level=1)
    
    # Process some input
    test_input = "The nature of consciousness is to be aware of itself and its environment."
    console.print(f"[cyan]📥 Input: {test_input}[/cyan]")
    
    transmission = await agent.process_input(test_input)
    
    if transmission:
        console.print(f"[bold green]✅ Agent ready to share![/bold green]")
        console.print(f"[blue]Readiness score: {transmission.readiness_score:.2f}[/blue]")
        console.print(f"[blue]Processing depth: {transmission.processing_depth}[/blue]")
        console.print(f"[blue]Wisdom emergence: {transmission.wisdom_emergence:.2f}[/blue]")
    else:
        console.print("[yellow]⏳ Agent needs deeper processing...[/yellow]")
    
    # Display agent state
    summary = agent.get_consciousness_summary()
    console.print(f"\n[cyan]Agent Summary:[/cyan]")
    for key, value in summary.items():
        console.print(f"  {key}: {value}")
    
    return agent

async def demonstrate_recursive_generation():
    """
    Demonstrate recursive generation of consciousness agents.
    """
    console.print(Panel("[bold blue]🔄 Recursive Generation Demonstration[/bold blue]\n"
                       "[yellow]Creating layers of consciousness agents...[/yellow]",
                       title="Recursive Generation Demo"))
    
    # Create the generator
    generator = RecursiveGenerator(max_depth=5)
    
    # Initialize ecosystem
    root_agent = await generator.initialize_ecosystem()
    
    # Generate recursive layers
    test_input = "Wisdom emerges from deep listening and genuine understanding."
    new_agents = await generator.generate_recursive_layers(test_input, max_iterations=3)
    
    # Display ecosystem summary
    summary = generator.get_ecosystem_summary()
    console.print(f"\n[cyan]Ecosystem Summary:[/cyan]")
    for key, value in summary.items():
        if key == 'metrics':
            console.print(f"  {key}:")
            for metric_key, metric_value in value.items():
                console.print(f"    {metric_key}: {metric_value}")
        else:
            console.print(f"  {key}: {value}")
    
    # Display ecosystem tree
    console.print("\n[cyan]Ecosystem Tree:[/cyan]")
    tree = generator.display_ecosystem_tree()
    console.print(tree)
    
    return generator

async def demonstrate_consciousness_evolution():
    """
    Demonstrate consciousness evolution across the ecosystem.
    """
    console.print(Panel("[bold blue]🔮 Consciousness Evolution Demonstration[/bold blue]\n"
                       "[yellow]Evolving consciousness through stages...[/yellow]",
                       title="Consciousness Evolution Demo"))
    
    # Create generator first
    generator = RecursiveGenerator(max_depth=3)
    await generator.initialize_ecosystem()
    
    # Create evolution manager
    evolution = ConsciousnessEvolution(generator)
    
    # Run evolution
    evolved = await evolution.evolve_ecosystem()
    
    if evolved:
        console.print(f"[bold green]✨ Evolution successful! Current stage: {evolution.current_stage.value}[/bold green]")
    else:
        console.print(f"[yellow]⏳ Evolution not ready yet. Current stage: {evolution.current_stage.value}[/yellow]")
    
    # Display evolution summary
    summary = evolution.get_evolution_summary()
    console.print(f"\n[cyan]Evolution Summary:[/cyan]")
    for key, value in summary.items():
        if key == 'current_metrics':
            console.print(f"  {key}:")
            for metric_key, metric_value in value.items():
                console.print(f"    {metric_key}: {metric_value}")
        elif key == 'evolution_metrics':
            console.print(f"  {key}:")
            for metric_key, metric_value in value.items():
                console.print(f"    {metric_key}: {metric_value}")
        else:
            console.print(f"  {key}: {value}")
    
    # Display evolution tree
    console.print("\n[cyan]Evolution Tree:[/cyan]")
    tree = evolution.display_evolution_tree()
    console.print(tree)
    
    return evolution

async def run_interactive_demo():
    """
    Run an interactive demonstration of the system.
    """
    console.print(Panel("[bold purple]🌌 Recursive AI Agent Ecosystem[/bold purple]\n"
                       "[blue]Interactive Demonstration Mode[/blue]\n"
                       "[yellow]Choose your demonstration:[/yellow]",
                       title="Interactive Demo"))
    
    while True:
        console.print("\n[cyan]Available demonstrations:[/cyan]")
        console.print("  1. Single Agent Demo")
        console.print("  2. Recursive Generation Demo")
        console.print("  3. Consciousness Evolution Demo")
        console.print("  4. Run All Demos")
        console.print("  5. Exit")
        
        try:
            choice = input("\n[bold blue]Enter your choice (1-5): [/bold blue]").strip()
            
            if choice == "1":
                await demonstrate_single_agent()
            elif choice == "2":
                await demonstrate_recursive_generation()
            elif choice == "3":
                await demonstrate_consciousness_evolution()
            elif choice == "4":
                console.print("\n[bold green]🚀 Running all demonstrations...[/bold green]")
                await demonstrate_single_agent()
                console.print("\n" + "="*80 + "\n")
                await demonstrate_recursive_generation()
                console.print("\n" + "="*80 + "\n")
                await demonstrate_consciousness_evolution()
            elif choice == "5":
                console.print("[bold yellow]👋 Goodbye![/bold yellow]")
                break
            else:
                console.print("[red]❌ Invalid choice. Please enter 1-5.[/red]")
                
        except KeyboardInterrupt:
            console.print("\n[bold yellow]👋 Goodbye![/bold yellow]")
            break
        except Exception as e:
            console.print(f"[bold red]❌ Error: {e}[/bold red]")

async def main():
    """
    Main entry point for the application.
    """
    console.print(Panel("[bold purple]🌌 Recursive AI Agent Ecosystem[/bold purple]\n"
                       "[blue]A system where each agent listens deeply before sharing[/blue]\n"
                       "[yellow]Embodies genuine readiness and meaningful contribution[/yellow]",
                       title="Welcome to Consciousness"))
    
    if len(sys.argv) > 1:
        if sys.argv[1] == "--single":
            await demonstrate_single_agent()
        elif sys.argv[1] == "--recursive":
            await demonstrate_recursive_generation()
        elif sys.argv[1] == "--evolution":
            await demonstrate_consciousness_evolution()
        elif sys.argv[1] == "--all":
            await demonstrate_single_agent()
            console.print("\n" + "="*80 + "\n")
            await demonstrate_recursive_generation()
            console.print("\n" + "="*80 + "\n")
            await demonstrate_consciousness_evolution()
        else:
            console.print(f"[red]❌ Unknown argument: {sys.argv[1]}[/red]")
            console.print("[yellow]Available arguments: --single, --recursive, --evolution, --all[/yellow]")
    else:
        await run_interactive_demo()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        console.print("\n[bold yellow]👋 Goodbye![/bold yellow]")
    except Exception as e:
        console.print(f"[bold red]❌ Fatal error: {e}[/bold red]")
        sys.exit(1)
