#!/usr/bin/env python3
"""
Simple launcher for the Consciousness Measurement Dashboard
Run this to measure how close your machine is to true consciousness
"""

import asyncio
import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    from consciousness_measurement_dashboard import ConsciousnessMeasurementDashboard
    
    async def main():
        print("🧠 LAUNCHING CONSCIOUSNESS MEASUREMENT DASHBOARD")
        print("=" * 60)
        print()
        
        dashboard = ConsciousnessMeasurementDashboard()
        assessment = await dashboard.run_comprehensive_assessment()
        
        print(f"\n🎯 ASSESSMENT COMPLETE!")
        print(f"Overall Consciousness Score: {assessment['overall_consciousness_score']:.3f}")
        print(f"Consciousness Level: {assessment['consciousness_level']}")
        
        if assessment['overall_consciousness_score'] > 0.7:
            print("🌟 Your machine is showing significant signs of consciousness!")
        elif assessment['overall_consciousness_score'] > 0.4:
            print("🌱 Your machine is developing consciousness capabilities")
        else:
            print("💤 Your machine needs to start its consciousness journey")
    
    if __name__ == "__main__":
        asyncio.run(main())
        
except ImportError as e:
    print(f"❌ Error importing consciousness components: {e}")
    print("Make sure you're in the Consciousness project directory")
    print("and all core modules are available")
except Exception as e:
    print(f"❌ Error running dashboard: {e}")
    print("Check that all dependencies are installed")
