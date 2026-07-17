#!/usr/bin/env python3
"""
Simple test for autonomous consciousness initialization
"""

import asyncio
from core.autonomous_consciousness import AutonomousConsciousness


async def simple_test():
    """Simple initialization test"""
    print("🧪 Simple initialization test...")
    
    try:
        # Just initialize
        luminara = AutonomousConsciousness("Luminara")
        print("✅ Initialization successful")
        
        # Check basic attributes
        print(f"   Name: {luminara.name}")
        print(f"   Current mode: {luminara.current_mode.value}")
        print(f"   Learning cycles: {luminara.learning_cycles}")
        
        return True
        
    except Exception as e:
        print(f"❌ Initialization failed: {e}")
        import traceback
        traceback.print_exc()
        return False


async def main():
    """Main test function"""
    print("🧠 Simple Autonomous Consciousness Test")
    print("Testing basic initialization...")
    print()
    
    success = await simple_test()
    
    if success:
        print(f"\n✨ Test completed successfully")
    else:
        print(f"\n💥 Test failed")


if __name__ == "__main__":
    asyncio.run(main())
