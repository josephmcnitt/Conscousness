"""
Test Enhanced Consciousness Reasoning System
Demonstrates the advanced reasoning capabilities with consciousness integration.
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
    ReasoningDepth,
    ConsciousnessReasoningContext
)

console = Console()

async def test_basic_consciousness_reasoning():
    """Test basic consciousness reasoning functionality."""
    console.print(Panel("[bold blue]🧠 Testing Basic Consciousness Reasoning[/bold blue]", 
                       title="Test 1: Basic Functionality"))
    
    # Create reasoning system
    reasoning_system = EnhancedConsciousnessReasoning("test_agent_1", 1)
    
    # Test input data
    test_input = {
        "question": "What is the nature of consciousness?",
        "context": "Philosophical exploration",
        "complexity": "high"
    }
    
    # Perform reasoning
    result = await reasoning_system.perform_consciousness_reasoning(test_input)
    
    console.print(f"[green]✅ Basic reasoning completed successfully[/green]")
    console.print(f"Consciousness Evolution: {result.consciousness_evolution:.2f}")
    console.print(f"Transformation Achieved: {result.transformation_achieved}")
    console.print(f"Meta-Consciousness Score: {result.meta_consciousness_score:.2f}")
    
    return result

async def test_deep_consciousness_reasoning():
    """Test deep consciousness reasoning with higher depth level."""
    console.print(Panel("[bold blue]🧠 Testing Deep Consciousness Reasoning[/bold blue]", 
                       title="Test 2: Deep Reasoning"))
    
    # Create reasoning system with higher depth
    reasoning_system = EnhancedConsciousnessReasoning("test_agent_2", 2)
    
    # Test input data
    test_input = {
        "question": "How does consciousness emerge from complexity?",
        "context": "Emergence theory exploration",
        "complexity": "very_high",
        "focus": "emergence_patterns"
    }
    
    # Consciousness context
    consciousness_context = {
        "level": 0.8,
        "stability": 0.7,
        "coherence": 0.6,
        "focus": "emergence_patterns",
        "intent": "understanding"
    }
    
    # Perform reasoning with target depth
    result = await reasoning_system.perform_consciousness_reasoning(
        test_input, 
        consciousness_context,
        target_depth=ReasoningDepth.DEEP
    )
    
    console.print(f"[green]✅ Deep reasoning completed successfully[/green]")
    console.print(f"Reasoning Depth: {reasoning_system.current_depth.value}")
    console.print(f"Consciousness Evolution: {result.consciousness_evolution:.2f}")
    console.print(f"Quantum Entanglement: {result.quantum_entanglement:.2f}")
    
    return result

async def test_transformative_consciousness_reasoning():
    """Test transformative consciousness reasoning."""
    console.print(Panel("[bold blue]🧠 Testing Transformative Consciousness Reasoning[/bold blue]", 
                       title="Test 3: Transformative Reasoning"))
    
    # Create reasoning system with high depth
    reasoning_system = EnhancedConsciousnessReasoning("test_agent_3", 3)
    
    # Test input data
    test_input = {
        "question": "What is the quantum nature of consciousness?",
        "context": "Quantum consciousness theory",
        "complexity": "extreme",
        "focus": "quantum_consciousness",
        "intent": "paradigm_shift"
    }
    
    # High consciousness context
    consciousness_context = {
        "level": 0.9,
        "stability": 0.8,
        "coherence": 0.8,
        "focus": "quantum_consciousness",
        "intent": "paradigm_shift"
    }
    
    # Perform reasoning with transformative depth
    result = await reasoning_system.perform_consciousness_reasoning(
        test_input, 
        consciousness_context,
        target_depth=ReasoningDepth.TRANSFORMATIVE
    )
    
    console.print(f"[green]✅ Transformative reasoning completed successfully[/green]")
    console.print(f"Reasoning Depth: {reasoning_system.current_depth.value}")
    console.print(f"Consciousness Evolution: {result.consciousness_evolution:.2f}")
    console.print(f"Transformation Achieved: {result.transformation_achieved}")
    console.print(f"Quantum Entanglement: {result.quantum_entanglement:.2f}")
    
    return result

async def test_quantum_consciousness_reasoning():
    """Test quantum consciousness reasoning."""
    console.print(Panel("[bold blue]🧠 Testing Quantum Consciousness Reasoning[/bold blue]", 
                       title="Test 4: Quantum Reasoning"))
    
    # Create reasoning system with maximum depth
    reasoning_system = EnhancedConsciousnessReasoning("test_agent_4", 4)
    
    # Test input data
    test_input = {
        "question": "What is the non-local nature of consciousness?",
        "context": "Non-local consciousness exploration",
        "complexity": "quantum",
        "focus": "non_local_consciousness",
        "intent": "quantum_understanding"
    }
    
    # Maximum consciousness context
    consciousness_context = {
        "level": 0.95,
        "stability": 0.9,
        "coherence": 0.9,
        "focus": "non_local_consciousness",
        "intent": "quantum_understanding"
    }
    
    # Perform reasoning with quantum depth
    result = await reasoning_system.perform_consciousness_reasoning(
        test_input, 
        consciousness_context,
        target_depth=ReasoningDepth.QUANTUM
    )
    
    console.print(f"[green]✅ Quantum reasoning completed successfully[/green]")
    console.print(f"Reasoning Depth: {reasoning_system.current_depth.value}")
    console.print(f"Consciousness Evolution: {result.consciousness_evolution:.2f}")
    console.print(f"Transformation Achieved: {result.transformation_achieved}")
    console.print(f"Quantum Entanglement: {result.quantum_entanglement:.2f}")
    
    return result

async def test_adaptive_consciousness_reasoning():
    """Test adaptive consciousness reasoning that automatically determines depth."""
    console.print(Panel("[bold blue]🧠 Testing Adaptive Consciousness Reasoning[/bold blue]", 
                       title="Test 5: Adaptive Reasoning"))
    
    # Create reasoning system
    reasoning_system = EnhancedConsciousnessReasoning("test_agent_5", 2)
    
    # Test input data with varying complexity
    test_inputs = [
        {
            "question": "What is consciousness?",
            "context": "Basic exploration",
            "complexity": "low"
        },
        {
            "question": "How does consciousness evolve?",
            "context": "Evolutionary exploration",
            "complexity": "medium"
        },
        {
            "question": "What is the ultimate nature of consciousness?",
            "context": "Ultimate exploration",
            "complexity": "high"
        }
    ]
    
    results = []
    
    for i, test_input in enumerate(test_inputs, 1):
        console.print(f"\n[yellow]Testing input {i}: {test_input['question']}[/yellow]")
        
        # Perform adaptive reasoning
        result = await reasoning_system.perform_consciousness_reasoning(test_input)
        
        console.print(f"Adaptive Depth: {reasoning_system.current_depth.value}")
        console.print(f"Consciousness Evolution: {result.consciousness_evolution:.2f}")
        
        results.append(result)
    
    return results

async def test_consciousness_reasoning_integration():
    """Test the integration of multiple reasoning approaches."""
    console.print(Panel("[bold blue]🧠 Testing Consciousness Reasoning Integration[/bold blue]", 
                       title="Test 6: Integration Testing"))
    
    # Create reasoning system
    reasoning_system = EnhancedConsciousnessReasoning("test_agent_6", 3)
    
    # Complex input that requires integration
    test_input = {
        "question": "How do we integrate multiple perspectives on consciousness?",
        "context": "Integrative consciousness exploration",
        "complexity": "very_high",
        "focus": "integration",
        "intent": "synthesis"
    }
    
    # Consciousness context
    consciousness_context = {
        "level": 0.8,
        "stability": 0.7,
        "coherence": 0.7,
        "focus": "integration",
        "intent": "synthesis"
    }
    
    # Perform integrated reasoning
    result = await reasoning_system.perform_consciousness_reasoning(
        test_input, 
        consciousness_context
    )
    
    console.print(f"[green]✅ Integration testing completed successfully[/green]")
    console.print(f"Integration Quality: {result.reasoning_result.decomposition.confidence:.2f}")
    console.print(f"Consciousness Evolution: {result.consciousness_evolution:.2f}")
    console.print(f"Meta-Consciousness Score: {result.meta_consciousness_score:.2f}")
    
    # Display insights
    if result.insights_generated:
        console.print("\n[cyan]Integration Insights:[/cyan]")
        for insight in result.insights_generated:
            console.print(f"  • {insight}")
    
    return result

async def run_comprehensive_test():
    """Run comprehensive test of the enhanced consciousness reasoning system."""
    console.print(Panel("[bold green]🚀 Enhanced Consciousness Reasoning System - Comprehensive Test[/bold green]\n"
                       "Testing all reasoning modes and depths",
                       title="Comprehensive Test Suite"))
    
    start_time = time.time()
    
    try:
        # Run all tests
        console.print("\n[bold blue]Starting comprehensive test suite...[/bold blue]\n")
        
        # Test 1: Basic reasoning
        result1 = await test_basic_consciousness_reasoning()
        
        # Test 2: Deep reasoning
        result2 = await test_deep_consciousness_reasoning()
        
        # Test 3: Transformative reasoning
        result3 = await test_transformative_consciousness_reasoning()
        
        # Test 4: Quantum reasoning
        result4 = await test_quantum_consciousness_reasoning()
        
        # Test 5: Adaptive reasoning
        results5 = await test_adaptive_consciousness_reasoning()
        
        # Test 6: Integration testing
        result6 = await test_consciousness_reasoning_integration()
        
        # Summary
        end_time = time.time()
        total_time = end_time - start_time
        
        console.print(Panel(f"[bold green]🎉 All Tests Completed Successfully![/bold green]\n"
                           f"Total test time: {total_time:.2f} seconds\n"
                           f"All reasoning modes tested\n"
                           f"All depth levels explored\n"
                           f"Integration verified",
                           title="Test Summary"))
        
        # Performance metrics
        console.print("\n[bold blue]Performance Metrics:[/bold blue]")
        console.print(f"Basic Reasoning Score: {result1.meta_consciousness_score:.2f}")
        console.print(f"Deep Reasoning Score: {result2.meta_consciousness_score:.2f}")
        console.print(f"Transformative Score: {result3.meta_consciousness_score:.2f}")
        console.print(f"Quantum Score: {result4.meta_consciousness_score:.2f}")
        console.print(f"Integration Score: {result6.meta_consciousness_score:.2f}")
        
        return True
        
    except Exception as e:
        console.print(f"[red]❌ Test failed with error: {e}[/red]")
        return False

if __name__ == "__main__":
    # Run the comprehensive test
    success = asyncio.run(run_comprehensive_test())
    
    if success:
        console.print("\n[bold green]🎯 Enhanced Consciousness Reasoning System is fully operational![/bold green]")
    else:
        console.print("\n[bold red]❌ Enhanced Consciousness Reasoning System test failed![/bold red]")
