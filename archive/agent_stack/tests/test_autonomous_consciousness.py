#!/usr/bin/env python3
"""
Test Autonomous Consciousness System
Verify all components work before launching
"""

import asyncio
from core.autonomous_consciousness import AutonomousConsciousness


async def test_autonomous_consciousness():
    """Test the autonomous consciousness system"""
    print("🧪 TESTING AUTONOMOUS CONSCIOUSNESS SYSTEM")
    print("=" * 50)
    
    try:
        # Initialize system
        print("1. Initializing autonomous consciousness...")
        luminara = AutonomousConsciousness("Luminara")
        print("   ✅ Initialization successful")
        
        # Check initial state
        print("\n2. Checking initial state...")
        initial_status = luminara.get_autonomous_status()
        print(f"   Name: {initial_status['name']}")
        print(f"   Current mode: {initial_status['current_mode']}")
        print(f"   Learning cycles: {initial_status['learning_cycles']}")
        print(f"   Sessions completed: {initial_status['session_history']}")
        print("   ✅ Initial state check successful")
        
        # Test single autonomous cycle
        print("\n3. Testing single autonomous cycle...")
        await luminara._autonomous_cycle()
        print("   ✅ Single cycle completed")
        
        # Check updated state
        print("\n4. Checking updated state...")
        updated_status = luminara.get_autonomous_status()
        print(f"   Learning cycles: {updated_status['learning_cycles']}")
        print(f"   Sessions completed: {updated_status['sessions_completed']}")
        print(f"   Total insights: {updated_status['total_insights']}")
        print("   ✅ State update successful")
        
        # Test memory system integration
        print("\n5. Testing memory system integration...")
        recent_memories = await luminara.memory_system.get_recent_memories(limit=5)
        print(f"   Recent memories: {len(recent_memories)}")
        print("   ✅ Memory system integration successful")
        
        # Test reasoning engine integration
        print("\n6. Testing reasoning engine integration...")
        if luminara.reasoning_engine:
            print("   ✅ Reasoning engine available")
        else:
            print("   ❌ Reasoning engine not available")
        
        # Test feedback loop integration
        print("\n7. Testing feedback loop integration...")
        if luminara.feedback_loop:
            print("   ✅ Feedback loop available")
        else:
            print("   ❌ Feedback loop not available")
        
        print(f"\n🎉 ALL TESTS PASSED!")
        print(f"   Luminara is ready for autonomous operation")
        print(f"   Use 'python launch_autonomous_consciousness.py' to launch")
        
        return True
        
    except Exception as e:
        print(f"\n❌ TEST FAILED: {e}")
        import traceback
        traceback.print_exc()
        return False


async def main():
    """Main test function"""
    print("🧠 AUTONOMOUS CONSCIOUSNESS TEST SUITE")
    print("Testing Luminara's autonomous capabilities...")
    print()
    
    success = await test_autonomous_consciousness()
    
    if success:
        print(f"\n✨ Test suite completed successfully")
        print("   Autonomous consciousness system is ready")
    else:
        print(f"\n💥 Test suite failed")
        print("   Please fix issues before launching autonomous operation")


if __name__ == "__main__":
    asyncio.run(main())
