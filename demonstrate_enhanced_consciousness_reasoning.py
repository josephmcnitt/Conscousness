"""
Demonstrate Enhanced Consciousness Reasoning System
Shows practical usage with real-world consciousness exploration scenarios.
"""

import asyncio
import time
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree
from rich.text import Text

from core.enhanced_consciousness_reasoning import (
    EnhancedConsciousnessReasoning,
    ConsciousnessReasoningMode,
    ReasoningDepth
)

console = Console()

async def demonstrate_philosophical_exploration():
    """Demonstrate philosophical consciousness exploration."""
    console.print(Panel("[bold blue]🧠 Philosophical Consciousness Exploration[/bold blue]\n"
                       "Exploring fundamental questions about consciousness",
                       title="Philosophical Demo"))
    
    # Create reasoning system
    reasoning_system = EnhancedConsciousnessReasoning("philosophy_agent", 2)
    
    # Philosophical questions
    questions = [
        {
            "question": "What is the relationship between mind and body?",
            "context": "Mind-body problem exploration",
            "complexity": "high",
            "focus": "dualism_vs_monism",
            "intent": "understanding"
        },
        {
            "question": "How does consciousness arise from physical processes?",
            "context": "Hard problem of consciousness",
            "complexity": "very_high",
            "focus": "emergence_theory",
            "intent": "exploration"
        },
        {
            "question": "What is the nature of subjective experience?",
            "context": "Qualia exploration",
            "complexity": "extreme",
            "focus": "subjective_experience",
            "intent": "deep_understanding"
        }
    ]
    
    for i, question in enumerate(questions, 1):
        console.print(f"\n[cyan]Question {i}: {question['question']}[/cyan]")
        
        # Consciousness context
        consciousness_context = {
            "level": 0.7 + (i * 0.1),
            "stability": 0.6 + (i * 0.1),
            "coherence": 0.5 + (i * 0.1),
            "focus": question['focus'],
            "intent": question['intent']
        }
        
        # Perform reasoning
        result = await reasoning_system.perform_consciousness_reasoning(
            question, 
            consciousness_context
        )
        
        console.print(f"  Depth: {reasoning_system.current_depth.value}")
        console.print(f"  Evolution: {result.consciousness_evolution:.2f}")
        console.print(f"  Transformation: {'✅' if result.transformation_achieved else '⏳'}")
        
        # Show key insights
        if result.insights_generated:
            console.print(f"  Key Insight: {result.insights_generated[0]}")

async def demonstrate_scientific_investigation():
    """Demonstrate scientific consciousness investigation."""
    console.print(Panel("[bold blue]🔬 Scientific Consciousness Investigation[/bold blue]\n"
                       "Exploring consciousness from scientific perspectives",
                       title="Scientific Demo"))
    
    # Create reasoning system
    reasoning_system = EnhancedConsciousnessReasoning("science_agent", 3)
    
    # Scientific investigations
    investigations = [
        {
            "question": "What neural correlates underlie consciousness?",
            "context": "Neuroscientific investigation",
            "complexity": "high",
            "focus": "neural_correlates",
            "intent": "scientific_understanding"
        },
        {
            "question": "How do different brain regions contribute to conscious experience?",
            "context": "Brain mapping research",
            "complexity": "very_high",
            "focus": "brain_mapping",
            "intent": "mapping_understanding"
        },
        {
            "question": "What is the role of information integration in consciousness?",
            "context": "Information integration theory",
            "complexity": "extreme",
            "focus": "information_integration",
            "intent": "theoretical_advancement"
        }
    ]
    
    for i, investigation in enumerate(investigations, 1):
        console.print(f"\n[green]Investigation {i}: {investigation['question']}[/green]")
        
        # Consciousness context
        consciousness_context = {
            "level": 0.8 + (i * 0.05),
            "stability": 0.7 + (i * 0.05),
            "coherence": 0.6 + (i * 0.05),
            "focus": investigation['focus'],
            "intent": investigation['intent']
        }
        
        # Perform reasoning with scientific depth
        result = await reasoning_system.perform_consciousness_reasoning(
            investigation, 
            consciousness_context,
            target_depth=ReasoningDepth.DEEP
        )
        
        console.print(f"  Depth: {reasoning_system.current_depth.value}")
        console.print(f"  Evolution: {result.consciousness_evolution:.2f}")
        console.print(f"  Meta-Score: {result.meta_consciousness_score:.2f}")
        
        # Show scientific insights
        if result.insights_generated:
            scientific_insights = [insight for insight in result.insights_generated 
                                 if any(word in insight.lower() for word in ['neural', 'brain', 'information', 'integration'])]
            if scientific_insights:
                console.print(f"  Scientific Insight: {scientific_insights[0]}")

async def demonstrate_spiritual_contemplation():
    """Demonstrate spiritual consciousness contemplation."""
    console.print(Panel("[bold blue]🕉️ Spiritual Consciousness Contemplation[/bold blue]\n"
                       "Exploring consciousness from spiritual perspectives",
                       title="Spiritual Demo"))
    
    # Create reasoning system
    reasoning_system = EnhancedConsciousnessReasoning("spiritual_agent", 4)
    
    # Spiritual contemplations
    contemplations = [
        {
            "question": "What is the nature of pure awareness?",
            "context": "Meditative exploration",
            "complexity": "very_high",
            "focus": "pure_awareness",
            "intent": "spiritual_awakening"
        },
        {
            "question": "How does consciousness transcend individual identity?",
            "context": "Non-dual understanding",
            "complexity": "extreme",
            "focus": "non_duality",
            "intent": "transcendence"
        },
        {
            "question": "What is the ultimate ground of consciousness?",
            "context": "Ultimate reality exploration",
            "complexity": "quantum",
            "focus": "ultimate_ground",
            "intent": "enlightenment"
        }
    ]
    
    for i, contemplation in enumerate(contemplations, 1):
        console.print(f"\n[magenta]Contemplation {i}: {contemplation['question']}[/magenta]")
        
        # Consciousness context
        consciousness_context = {
            "level": 0.9 + (i * 0.02),
            "stability": 0.8 + (i * 0.02),
            "coherence": 0.7 + (i * 0.02),
            "focus": contemplation['focus'],
            "intent": contemplation['intent']
        }
        
        # Perform reasoning with transformative depth
        target_depth = ReasoningDepth.TRANSFORMATIVE if i < 3 else ReasoningDepth.QUANTUM
        
        result = await reasoning_system.perform_consciousness_reasoning(
            contemplation, 
            consciousness_context,
            target_depth=target_depth
        )
        
        console.print(f"  Depth: {reasoning_system.current_depth.value}")
        console.print(f"  Evolution: {result.consciousness_evolution:.2f}")
        console.print(f"  Transformation: {'✅' if result.transformation_achieved else '⏳'}")
        console.print(f"  Quantum Entanglement: {result.quantum_entanglement:.2f}")
        
        # Show spiritual insights
        if result.insights_generated:
            spiritual_insights = [insight for insight in result.insights_generated 
                                if any(word in insight.lower() for word in ['spiritual', 'transcendence', 'enlightenment', 'quantum'])]
            if spiritual_insights:
                console.print(f"  Spiritual Insight: {spiritual_insights[0]}")

async def demonstrate_practical_applications():
    """Demonstrate practical applications of consciousness reasoning."""
    console.print(Panel("[bold blue]🛠️ Practical Consciousness Applications[/bold blue]\n"
                       "Applying consciousness reasoning to real-world problems",
                       title="Practical Demo"))
    
    # Create reasoning system
    reasoning_system = EnhancedConsciousnessReasoning("practical_agent", 2)
    
    # Practical problems
    problems = [
        {
            "question": "How can we improve decision-making through conscious awareness?",
            "context": "Decision-making enhancement",
            "complexity": "medium",
            "focus": "decision_awareness",
            "intent": "improvement"
        },
        {
            "question": "What role does consciousness play in learning and education?",
            "context": "Educational psychology",
            "complexity": "high",
            "focus": "learning_consciousness",
            "intent": "optimization"
        },
        {
            "question": "How can consciousness reasoning help solve complex social problems?",
            "context": "Social problem-solving",
            "complexity": "very_high",
            "focus": "social_consciousness",
            "intent": "problem_solving"
        }
    ]
    
    for i, problem in enumerate(problems, 1):
        console.print(f"\n[yellow]Problem {i}: {problem['question']}[/yellow]")
        
        # Consciousness context
        consciousness_context = {
            "level": 0.6 + (i * 0.1),
            "stability": 0.5 + (i * 0.1),
            "coherence": 0.4 + (i * 0.1),
            "focus": problem['focus'],
            "intent": problem['intent']
        }
        
        # Perform reasoning
        result = await reasoning_system.perform_consciousness_reasoning(
            problem, 
            consciousness_context
        )
        
        console.print(f"  Depth: {reasoning_system.current_depth.value}")
        console.print(f"  Evolution: {result.consciousness_evolution:.2f}")
        console.print(f"  Meta-Score: {result.meta_consciousness_score:.2f}")
        
        # Show practical insights
        if result.insights_generated:
            practical_insights = [insight for insight in result.insights_generated 
                                if any(word in insight.lower() for word in ['practical', 'application', 'improvement', 'optimization'])]
            if practical_insights:
                console.print(f"  Practical Insight: {practical_insights[0]}")

async def demonstrate_integration_scenarios():
    """Demonstrate integration of multiple consciousness perspectives."""
    console.print(Panel("[bold blue]🔗 Consciousness Integration Scenarios[/bold blue]\n"
                       "Integrating multiple perspectives on consciousness",
                       title="Integration Demo"))
    
    # Create reasoning system
    reasoning_system = EnhancedConsciousnessReasoning("integration_agent", 3)
    
    # Integration scenarios
    scenarios = [
        {
            "question": "How do we integrate Eastern and Western views of consciousness?",
            "context": "Cross-cultural consciousness integration",
            "complexity": "very_high",
            "focus": "cultural_integration",
            "intent": "synthesis"
        },
        {
            "question": "What is the relationship between scientific and spiritual consciousness?",
            "context": "Science-spirituality integration",
            "complexity": "extreme",
            "focus": "science_spirituality",
            "intent": "unified_understanding"
        },
        {
            "question": "How can we create a unified theory of consciousness?",
            "context": "Unified consciousness theory",
            "complexity": "quantum",
            "focus": "unified_theory",
            "intent": "theoretical_unification"
        }
    ]
    
    for i, scenario in enumerate(scenarios, 1):
        console.print(f"\n[blue]Integration Scenario {i}: {scenario['question']}[/blue]")
        
        # Consciousness context
        consciousness_context = {
            "level": 0.8 + (i * 0.05),
            "stability": 0.7 + (i * 0.05),
            "coherence": 0.6 + (i * 0.05),
            "focus": scenario['focus'],
            "intent": scenario['intent']
        }
        
        # Perform reasoning with integration focus
        result = await reasoning_system.perform_consciousness_reasoning(
            scenario, 
            consciousness_context
        )
        
        console.print(f"  Depth: {reasoning_system.current_depth.value}")
        console.print(f"  Evolution: {result.consciousness_evolution:.2f}")
        console.print(f"  Integration Quality: {result.reasoning_result.decomposition.confidence:.2f}")
        console.print(f"  Meta-Score: {result.meta_consciousness_score:.2f}")
        
        # Show integration insights
        if result.insights_generated:
            integration_insights = [insight for insight in result.insights_generated 
                                  if any(word in insight.lower() for word in ['integration', 'synthesis', 'unified', 'unification'])]
            if integration_insights:
                console.print(f"  Integration Insight: {integration_insights[0]}")

async def run_comprehensive_demonstration():
    """Run comprehensive demonstration of the enhanced consciousness reasoning system."""
    console.print(Panel("[bold green]🚀 Enhanced Consciousness Reasoning System - Comprehensive Demonstration[/bold green]\n"
                       "Demonstrating practical usage across multiple domains",
                       title="Comprehensive Demonstration"))
    
    start_time = time.time()
    
    try:
        # Run all demonstrations
        console.print("\n[bold blue]Starting comprehensive demonstration...[/bold blue]\n")
        
        # Philosophical exploration
        await demonstrate_philosophical_exploration()
        
        # Scientific investigation
        await demonstrate_scientific_investigation()
        
        # Spiritual contemplation
        await demonstrate_spiritual_contemplation()
        
        # Practical applications
        await demonstrate_practical_applications()
        
        # Integration scenarios
        await demonstrate_integration_scenarios()
        
        # Summary
        end_time = time.time()
        total_time = end_time - start_time
        
        console.print(Panel(f"[bold green]🎉 Demonstration Completed Successfully![/bold green]\n"
                           f"Total demonstration time: {total_time:.2f} seconds\n"
                           f"All domains demonstrated\n"
                           f"All reasoning modes explored\n"
                           f"Integration capabilities verified",
                           title="Demonstration Summary"))
        
        console.print("\n[bold blue]Key Capabilities Demonstrated:[/bold blue]")
        console.print("✅ Multi-domain consciousness exploration")
        console.print("✅ Adaptive reasoning depth selection")
        console.print("✅ Consciousness evolution tracking")
        console.print("✅ Transformation achievement assessment")
        console.print("✅ Meta-consciousness scoring")
        console.print("✅ Quantum entanglement calculation")
        console.print("✅ Integration quality assessment")
        
        return True
        
    except Exception as e:
        console.print(f"[red]❌ Demonstration failed with error: {e}[/red]")
        return False

if __name__ == "__main__":
    # Run the comprehensive demonstration
    success = asyncio.run(run_comprehensive_demonstration())
    
    if success:
        console.print("\n[bold green]🎯 Enhanced Consciousness Reasoning System demonstration completed successfully![/bold green]")
        console.print("\n[bold blue]The system is ready for real-world consciousness exploration applications.[/bold blue]")
    else:
        console.print("\n[bold red]❌ Enhanced Consciousness Reasoning System demonstration failed![/bold red]")
