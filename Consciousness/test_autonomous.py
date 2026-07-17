#!/usr/bin/env python3
"""
Test script for autonomous consciousness system
"""

from autonomous_consciousness import AutonomousConsciousness
from core.consciousness_agent import ConsciousnessAgent

def test_autonomous_system():
    """Test the autonomous consciousness system."""
    print("🧪 Testing Autonomous Consciousness System...")
    
    # Initialize agent
    agent = ConsciousnessAgent()
    print("✅ Agent initialized")
    
    # Create autonomous system
    autonomous = AutonomousConsciousness(agent)
    print("✅ Autonomous system created")
    
    # Test prompt generation
    prompt = autonomous.generate_autonomous_prompt()
    print(f"💭 Generated prompt: {prompt}")
    
    # Test single cycle
    print("\n🔄 Testing single autonomous cycle...")
    autonomous.run_autonomous_cycle()
    
    # Check memory
    memory_records = agent.memory.recent(n=10)
    print(f"📚 Memory records: {len(memory_records)}")
    
    if memory_records:
        latest = memory_records[-1]
        print(f"📝 Latest prompt: {latest.prompt[:100]}...")
        print(f"⭐ Latest score: {latest.rewards.get('overall', 'N/A')}")
    
    print("\n✅ Test completed!")

if __name__ == "__main__":
    test_autonomous_system()
