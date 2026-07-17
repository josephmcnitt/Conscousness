#!/usr/bin/env python3
"""
Test autonomous cycle execution
"""

import asyncio
from core.autonomous_consciousness import AutonomousConsciousness


async def cycle_test():
    """Test autonomous cycle execution"""
    print("🧪 Testing autonomous cycle...")
    
    try:
        # Initialize
        luminara = AutonomousConsciousness("Luminara")
        print("✅ Initialization successful")
        
        # Run one cycle
        print("🔄 Running autonomous cycle...")
        await luminara._autonomous_cycle()
        print("✅ Cycle completed")
        
        # Check results
        status = luminara.get_autonomous_status()
        print(f"   Learning cycles: {status['learning_cycles']}")
        print(f"   Sessions completed: {status['sessions_completed']}")
        
        return True
        
    except Exception as e:
        print(f"❌ Cycle test failed: {e}")
        import traceback
        traceback.print_exc()
        return False


async def main():
    """Main test function"""
    print("🧠 Autonomous Cycle Test")
    print("Testing single cycle execution...")
    print()
    
    success = await cycle_test()
    
    if success:
        print(f"\n✨ Cycle test completed successfully")
    else:
        print(f"\n💥 Cycle test failed")


if __name__ == "__main__":
    asyncio.run(main())
