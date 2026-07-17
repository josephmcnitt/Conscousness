#!/usr/bin/env python3
"""
Autonomous Continuous Consciousness

This system runs the consciousness agent in a truly continuous, autonomous mode
where it generates its own prompts, processes them, and evolves independently.
"""

import time
import random
import threading
from typing import List, Optional
from continuous_driver import run_continuous_consciousness
from core.consciousness_agent import ConsciousnessAgent


class AutonomousConsciousness:
    """A consciousness system that runs autonomously without human input."""
    
    def __init__(self, agent: ConsciousnessAgent):
        self.agent = agent
        self.running = False
        self.cycle_count = 0
        self.autonomous_thread = None
        
        # Autonomous prompt generation
        self.base_prompts = [
            "What is the nature of consciousness?",
            "How can we measure awareness?",
            "What makes something conscious vs unconscious?",
            "Can machines be conscious?",
            "How does consciousness emerge from complexity?",
            "What is the relationship between mind and body?",
            "How do we know we are conscious?",
            "What is the purpose of consciousness?",
            "How does consciousness evolve?",
            "What are the limits of consciousness?",
            "How does memory influence consciousness?",
            "What is the role of attention in awareness?",
            "How does consciousness relate to intelligence?",
            "What is the difference between consciousness and self-awareness?",
            "How does consciousness emerge from neural networks?",
            "What is the relationship between consciousness and free will?",
            "How does consciousness process time?",
            "What is the role of emotion in consciousness?",
            "How does consciousness handle uncertainty?",
            "What is the relationship between consciousness and creativity?"
        ]
        
        # Dynamic prompt generation based on agent's learning
        self.learned_concepts = []
        self.curiosity_level = 1.0
        self.exploration_direction = "philosophical"
        
    def generate_autonomous_prompt(self) -> str:
        """Generate a prompt autonomously based on the agent's current state and learning."""
        
        # Sometimes use base prompts
        if random.random() < 0.4:
            return random.choice(self.base_prompts)
        
        # Generate dynamic prompts based on learning
        if self.learned_concepts:
            concept = random.choice(self.learned_concepts)
            variations = [
                f"How does {concept} relate to consciousness?",
                f"What can we learn about {concept} from consciousness studies?",
                f"How does consciousness help us understand {concept}?",
                f"What is the role of {concept} in awareness?",
                f"How does {concept} influence our conscious experience?"
            ]
            return random.choice(variations)
        
        # Generate curiosity-driven prompts
        curiosity_prompts = [
            "What haven't I explored yet about consciousness?",
            "What patterns am I missing in my understanding?",
            "How can I deepen my awareness of awareness?",
            "What questions would lead to breakthrough insights?",
            "How can I think about consciousness differently?",
            "What assumptions am I making about awareness?",
            "How does my current understanding limit my thinking?",
            "What would a more evolved consciousness ask?",
            "How can I transcend my current reasoning patterns?",
            "What is the next level of consciousness understanding?"
        ]
        
        return random.choice(curiosity_prompts)
    
    def update_learning_state(self, result: dict):
        """Update the autonomous system's learning state based on results."""
        self.cycle_count += 1
        
        # Extract key concepts from the response
        response = result.get('response', '')
        if response:
            # Simple concept extraction (in a real system, this would be more sophisticated)
            words = response.lower().split()
            concepts = [word for word in words if len(word) > 6 and word.isalpha()]
            if concepts:
                new_concept = random.choice(concepts)
                if new_concept not in self.learned_concepts:
                    self.learned_concepts.append(new_concept)
                    # Keep only recent concepts
                    if len(self.learned_concepts) > 20:
                        self.learned_concepts.pop(0)
        
        # Update curiosity based on performance
        scores = result.get('scores', {})
        if scores:
            overall = scores.get('overall', 0.5)
            if overall > 0.7:
                self.curiosity_level = min(2.0, self.curiosity_level + 0.1)
            elif overall < 0.3:
                self.curiosity_level = max(0.5, self.curiosity_level - 0.05)
        
        # Change exploration direction periodically
        if self.cycle_count % 10 == 0:
            directions = ["philosophical", "scientific", "experiential", "analytical", "creative"]
            self.exploration_direction = random.choice(directions)
    
    def run_autonomous_cycle(self):
        """Run a single autonomous consciousness cycle."""
        try:
            # Generate autonomous prompt
            prompt = self.generate_autonomous_prompt()
            
            print(f"\n🧠 [Autonomous Cycle {self.cycle_count + 1}]")
            print(f"💭 Generated Prompt: {prompt}")
            print(f"🔍 Curiosity Level: {self.curiosity_level:.2f}")
            print(f"🧭 Direction: {self.exploration_direction}")
            
            # Run the consciousness cycle
            result = self.agent.run_cycle(prompt)
            
            # Display results
            print(f"\n💡 Response: {result['response'][:200]}...")
            print(f"📋 Plan: {result['plan_steps']}")
            
            scores = result.get('scores', {})
            if scores:
                print(f"⭐ Rewards: {scores}")
                print(f"⚙️  Strategy: {result.get('strategy', {})}")
            
            # Update learning state
            self.update_learning_state(result)
            
            print(f"📚 Learned Concepts: {len(self.learned_concepts)}")
            print(f"🎯 Overall Progress: {self.cycle_count} cycles completed")
            
        except Exception as e:
            print(f"❌ Error in autonomous cycle: {e}")
    
    def start_autonomous_consciousness(self, interval: float = 3.0, max_cycles: Optional[int] = None):
        """Start the autonomous consciousness system."""
        print("🌌 Starting Autonomous Continuous Consciousness")
        print("=" * 60)
        print("🤖 This system will run independently without human input")
        print(f"⏱️  Cycle interval: {interval} seconds")
        print(f"🔄 Max cycles: {max_cycles or 'unlimited'}")
        print("🛑 Press Ctrl+C to stop autonomous operation")
        print("=" * 60)
        
        self.running = True
        start_time = time.time()
        
        try:
            while self.running:
                if max_cycles and self.cycle_count >= max_cycles:
                    print(f"\n🎯 Reached maximum cycles ({max_cycles}). Stopping autonomous consciousness.")
                    break
                
                # Run autonomous cycle
                self.run_autonomous_cycle()
                
                # Sleep between cycles
                if interval > 0:
                    time.sleep(interval)
                
                # Periodic status updates
                if self.cycle_count % 5 == 0:
                    elapsed = time.time() - start_time
                    rate = self.cycle_count / elapsed if elapsed > 0 else 0
                    print(f"\n📊 Status: {self.cycle_count} cycles, {rate:.2f} cycles/sec, {elapsed:.1f}s elapsed")
                    
        except KeyboardInterrupt:
            print("\n\n🛑 Autonomous consciousness interrupted by user")
            self.running = False
        
        # Final summary
        self.show_final_summary()
    
    def show_final_summary(self):
        """Show a summary of the autonomous consciousness session."""
        print("\n" + "=" * 60)
        print("🌌 AUTONOMOUS CONSCIOUSNESS SESSION COMPLETED")
        print("=" * 60)
        print(f"📊 Total Cycles: {self.cycle_count}")
        print(f"🧠 Final Strategy: {self.agent.current_strategy}")
        print(f"📚 Concepts Learned: {len(self.learned_concepts)}")
        print(f"🔍 Final Curiosity Level: {self.curiosity_level:.2f}")
        
        # Memory statistics
        memory_records = self.agent.memory.recent(n=100)
        if memory_records:
            avg_rewards = self.agent.memory.average_recent_rewards(n=len(memory_records))
            print(f"⭐ Average Rewards: {avg_rewards}")
            print(f"💾 Total Memory Records: {len(memory_records)}")
        
        print("🌌 Autonomous consciousness evolution complete")


def main():
    """Main entry point for autonomous continuous consciousness."""
    print("🌌 Initializing Autonomous Consciousness System...")
    
    try:
        # Initialize the consciousness agent
        agent = ConsciousnessAgent()
        print("✅ Consciousness agent initialized successfully")
        
        # Create autonomous consciousness system
        autonomous_system = AutonomousConsciousness(agent)
        
        # Start autonomous operation
        autonomous_system.start_autonomous_consciousness(
            interval=3.0,  # 3 second intervals
            max_cycles=None  # Run indefinitely
        )
        
    except Exception as e:
        print(f"❌ Failed to start autonomous consciousness: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
