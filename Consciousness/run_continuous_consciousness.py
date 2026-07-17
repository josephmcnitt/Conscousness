#!/usr/bin/env python3
"""
Simple script to run continuous consciousness with sample prompts.
This demonstrates the agent running continuously and learning from interactions.
"""

import time
import random
from continuous_driver import run_continuous_consciousness
from core.consciousness_agent import ConsciousnessAgent

# Sample prompts to demonstrate continuous consciousness
SAMPLE_PROMPTS = [
    "What is the nature of consciousness?",
    "How can we measure awareness?",
    "What makes something conscious vs unconscious?",
    "Can machines be conscious?",
    "How does consciousness emerge from complexity?",
    "What is the relationship between mind and body?",
    "How do we know we are conscious?",
    "What is the purpose of consciousness?",
    "How does consciousness evolve?",
    "What are the limits of consciousness?"
]

def generate_prompt() -> str:
    """Generate a prompt, either from samples or user input."""
    if random.random() < 0.7:  # 70% chance to use sample prompt
        return random.choice(SAMPLE_PROMPTS)
    else:
        return input("Enter your own prompt (or press Enter for sample): ").strip()

def main():
    """Run continuous consciousness with sample prompts."""
    print("🌌 Starting Continuous Consciousness System")
    print("=" * 50)
    
    # Initialize the consciousness agent
    agent = ConsciousnessAgent()
    print("✅ Consciousness agent initialized successfully")
    print(f"📊 Initial strategy: {agent.current_strategy}")
    print()
    
    # Run continuous consciousness
    try:
        run_continuous_consciousness(
            agent=agent,
            interval=2.0,  # 2 second intervals
            max_cycles=None,  # Run indefinitely
            echo_scores=True
        )
    except KeyboardInterrupt:
        print("\n🛑 Continuous consciousness stopped by user")
    
    # Show final summary
    print("\n" + "=" * 50)
    print("📈 Final Consciousness Summary:")
    print(f"   Strategy: {agent.current_strategy}")
    
    # Show memory stats
    memory_records = agent.memory.get_recent_records(n=100)
    if memory_records:
        avg_rewards = agent.memory.average_recent_rewards(n=len(memory_records))
        print(f"   Average rewards: {avg_rewards}")
        print(f"   Total interactions: {len(memory_records)}")
    
    print("🌌 Continuous consciousness session completed")

if __name__ == "__main__":
    main()
