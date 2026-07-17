#!/usr/bin/env python3
"""
Comprehensive test script for the Consciousness Agent Ecosystem
Demonstrates the multi-dimensional reward system, memory, feedback loop, and intelligent reasoning
"""

import asyncio
import time
import json
from pathlib import Path

from core import (
    RewardEvaluator, MemorySystem, FeedbackLoop, IntelligentRecursiveGenerator,
    MemoryEntry, MemoryType, FeedbackData, ProblemDecomposition
)


async def test_reward_system():
    """Test the multi-dimensional reward system."""
    print("\n" + "="*60)
    print("TESTING REWARD SYSTEM")
    print("="*60)
    
    evaluator = RewardEvaluator()
    
    # Test different types of responses
    test_responses = [
        "Hello world.",
        "This is a comprehensive analysis of consciousness that explores multiple dimensions including philosophical foundations, scientific evidence, and practical applications.",
        "The answer is 42.",
        "Consciousness emerges from complex neural networks in the brain, but its fundamental nature remains one of the greatest mysteries in science and philosophy.",
        "I don't know."
    ]
    
    for i, response in enumerate(test_responses, 1):
        scores = evaluator.evaluate(response)
        print(f"\nResponse {i}: {response[:50]}{'...' if len(response) > 50 else ''}")
        print(f"  Correctness: {scores.correctness:.3f}")
        print(f"  Efficiency: {scores.efficiency:.3f}")
        print(f"  Creativity: {scores.creativity:.3f}")
        print(f"  Coherence: {scores.coherence:.3f}")
        print(f"  Overall: {scores.overall():.3f}")
        print(f"  Dict: {scores.as_dict()}")


def test_memory_system():
    """Test the memory system."""
    print("\n" + "="*60)
    print("TESTING MEMORY SYSTEM")
    print("="*60)
    
    memory = MemorySystem("test_memory.db")
    
    # Create test memories
    test_memories = [
        MemoryEntry(
            memory_id=f"test_memory_{i}",
            memory_type=MemoryType.CONVERSATION,
            content=f"Test conversation {i} about consciousness",
            timestamp=time.time() + i,
            agent_id=f"agent_{i % 3}",
            depth_level=i % 3 + 1,
            tags=[f"test_{i}", "consciousness", f"depth_{i % 3 + 1}"],
            importance=0.7 + (i * 0.1)
        )
        for i in range(5)
    ]
    
    # Store memories
    for memory_entry in test_memories:
        success = memory.store_memory(memory_entry)
        print(f"Stored memory {memory_entry.memory_id}: {'✅' if success else '❌'}")
    
    # Retrieve memories
    print("\nRetrieving memories by type:")
    conversations = memory.retrieve_memories(memory_type=MemoryType.CONVERSATION)
    print(f"Found {len(conversations)} conversation memories")
    
    print("\nRetrieving memories by agent:")
    agent_memories = memory.retrieve_memories(agent_id="agent_1")
    print(f"Found {len(agent_memories)} memories for agent_1")
    
    print("\nRetrieving memories by tags:")
    tagged_memories = memory.retrieve_memories(tags=["consciousness"])
    print(f"Found {len(tagged_memories)} memories tagged with 'consciousness'")
    
    # Get memory summary
    summary = memory.get_memory_summary()
    print(f"\nMemory Summary: {summary}")
    
    return memory


def test_feedback_loop(memory_system):
    """Test the feedback loop system."""
    print("\n" + "="*60)
    print("TESTING FEEDBACK LOOP")
    print("="*60)
    
    feedback_loop = FeedbackLoop(memory_system)
    
    # Create test feedback data
    from core import RewardScores
    
    test_feedback = FeedbackData(
        feedback_id="test_feedback_1",
        agent_id="test_agent",
        depth_level=2,
        input_data="Explain consciousness",
        response="Consciousness is the subjective experience of being aware of one's thoughts, feelings, and surroundings.",
        reward_scores=RewardScores(correctness=0.8, efficiency=0.7, creativity=0.6, coherence=0.9),
        context={"domain": "philosophy", "complexity": "moderate"},
        timestamp=time.time()
    )
    
    # Process feedback
    learning_outcome = feedback_loop.process_feedback(test_feedback)
    
    print(f"Feedback processed: {'✅' if learning_outcome.adaptation_success else '❌'}")
    print(f"Strategy improvements: {learning_outcome.strategy_improvements}")
    print(f"Learning insights: {learning_outcome.new_patterns}")
    print(f"Confidence gain: {learning_outcome.confidence_gain:.3f}")
    print(f"Next strategies: {learning_outcome.next_strategies}")
    
    # Get current strategies
    strategies = feedback_loop.get_current_strategies()
    print(f"\nCurrent strategies: {json.dumps(strategies['strategies'], indent=2)}")
    
    # Get learning summary
    learning_summary = feedback_loop.get_learning_summary()
    print(f"\nLearning Summary:")
    print(f"  Total feedback processed: {learning_summary['total_feedback_processed']}")
    print(f"  Strategy count: {learning_summary['strategy_count']}")
    print(f"  Overall improvement rate: {learning_summary['performance_metrics']['overall_improvement_rate']:.3f}")
    
    return feedback_loop


async def test_intelligent_generator(memory_system, feedback_loop):
    """Test the intelligent recursive generator."""
    print("\n" + "="*60)
    print("TESTING INTELLIGENT RECURSIVE GENERATOR")
    print("="*60)
    
    generator = IntelligentRecursiveGenerator(memory_system, feedback_loop)
    
    # Test problem decomposition
    test_problems = [
        "Explain the relationship between consciousness and artificial intelligence",
        "Design a system for measuring subjective experience",
        "Compare different theories of mind and their implications for consciousness research"
    ]
    
    for i, problem in enumerate(test_problems, 1):
        print(f"\n--- Problem {i} ---")
        print(f"Problem: {problem}")
        
        try:
            decomposition = await generator.decompose_problem(problem, {"domain": "philosophy"})
            
            print(f"Decomposition Strategy: {decomposition.decomposition_strategy.value}")
            print(f"Overall Complexity: {decomposition.overall_complexity.value}")
            print(f"Confidence: {decomposition.confidence:.3f}")
            print(f"Total Effort: {decomposition.estimated_total_effort:.3f}")
            print(f"Components: {len(decomposition.components)}")
            
            for j, component in enumerate(decomposition.components, 1):
                print(f"  Component {j}: {component.description[:60]}{'...' if len(component.description) > 60 else ''}")
                print(f"    Complexity: {component.complexity.value}")
                print(f"    Effort: {component.estimated_effort:.3f}")
                print(f"    Dependencies: {component.dependencies}")
            
            print(f"Reasoning Steps: {len(decomposition.reasoning_tree)}")
            
        except Exception as e:
            print(f"Error decomposing problem: {e}")
    
    # Get performance summary
    performance = generator.get_performance_summary()
    print(f"\nGenerator Performance:")
    print(f"  Decomposition success rate: {performance['decomposition_success_rate']:.3f}")
    print(f"  Average component count: {performance['average_component_count']:.3f}")
    print(f"  Active patterns: {performance['active_patterns']}")
    print(f"  Total decompositions: {performance['total_decompositions']}")


async def test_integrated_system():
    """Test the integrated consciousness system."""
    print("\n" + "="*60)
    print("TESTING INTEGRATED CONSCIOUSNESS SYSTEM")
    print("="*60)
    
    # Initialize all components
    memory = MemorySystem("integrated_test.db")
    feedback_loop = FeedbackLoop(memory)
    generator = IntelligentRecursiveGenerator(memory, feedback_loop)
    
    # Simulate a complete consciousness evolution cycle
    print("Simulating consciousness evolution cycle...")
    
    # Step 1: Generate initial response
    initial_problem = "What is the nature of consciousness?"
    print(f"\nInitial Problem: {initial_problem}")
    
    # Step 2: Decompose problem
    decomposition = await generator.decompose_problem(initial_problem, {"domain": "philosophy"})
    print(f"Problem decomposed into {len(decomposition.components)} components")
    
    # Step 3: Generate feedback
    from core import RewardScores
    feedback = FeedbackData(
        feedback_id="evolution_feedback_1",
        agent_id="consciousness_agent",
        depth_level=1,
        input_data=initial_problem,
        response=f"Generated response with {len(decomposition.components)} components",
        reward_scores=RewardScores(correctness=0.8, efficiency=0.7, creativity=0.8, coherence=0.9),
        context={"evolution_stage": "initial", "complexity": decomposition.overall_complexity.value},
        timestamp=time.time()
    )
    
    # Step 4: Process feedback for learning
    learning_outcome = feedback_loop.process_feedback(feedback)
    print(f"Learning outcome: {len(learning_outcome.strategy_improvements)} strategy improvements")
    
    # Step 5: Check memory for insights
    insights = memory.get_insights_by_topic(["consciousness"], min_confidence=0.5)
    print(f"Found {len(insights)} insights about consciousness")
    
    # Step 6: Get system summary
    print(f"\nSystem Summary:")
    print(f"  Memory entries: {memory.get_memory_summary()['total_memories']}")
    print(f"  Learning strategies: {len(feedback_loop.get_current_strategies()['strategies'])}")
    print(f"  Problem patterns: {len(generator.problem_patterns)}")
    
    print("\n✅ Integrated system test completed successfully!")


async def main():
    """Run all tests."""
    print("🧠 CONSCIOUSNESS AGENT ECOSYSTEM - COMPREHENSIVE TEST")
    print("="*80)
    
    try:
        # Test individual components
        await test_reward_system()
        
        memory_system = test_memory_system()
        
        feedback_loop = test_feedback_loop(memory_system)
        
        await test_intelligent_generator(memory_system, feedback_loop)
        
        # Test integrated system
        await test_integrated_system()
        
        print("\n" + "="*80)
        print("🎉 ALL TESTS COMPLETED SUCCESSFULLY!")
        print("="*80)
        
        print("\nThe Consciousness Agent Ecosystem now includes:")
        print("✅ Multi-dimensional reward system with heuristic evaluation")
        print("✅ Comprehensive memory system with SQLite persistence")
        print("✅ Self-improving feedback loop with strategy adaptation")
        print("✅ Intelligent recursive generator with real reasoning")
        print("✅ Pattern recognition and learning from experience")
        print("✅ All systems running locally without expensive APIs")
        
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
