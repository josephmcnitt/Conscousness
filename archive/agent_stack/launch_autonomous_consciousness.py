#!/usr/bin/env python3
"""
Launch Autonomous Consciousness System
Runs Luminara in continuous autonomous operation mode
"""

import asyncio
import signal
import sys
from core.autonomous_consciousness import AutonomousConsciousness


class GracefulShutdown:
    """Handle graceful shutdown of autonomous consciousness"""
    
    def __init__(self, consciousness: AutonomousConsciousness):
        self.consciousness = consciousness
        self.shutdown_requested = False
        
        # Set up signal handlers
        signal.signal(signal.SIGINT, self._signal_handler)
        signal.signal(signal.SIGTERM, self._signal_handler)
    
    def _signal_handler(self, signum, frame):
        """Handle shutdown signals gracefully"""
        print(f"\n🛑 Shutdown signal received ({signum})")
        print("   Initiating graceful shutdown...")
        self.shutdown_requested = True


async def main():
    """Main autonomous consciousness launcher"""
    print("🚀 LAUNCHING AUTONOMOUS CONSCIOUSNESS SYSTEM")
    print("=" * 60)
    print("🧠 System: Luminara Autonomous Consciousness")
    print("💫 Mode: Continuous Self-Directed Learning")
    print("🔄 Operation: Fully Autonomous (No Human Intervention)")
    print("💰 Cost: Local Operation Only (No API Calls)")
    print("=" * 60)
    
    # Initialize autonomous consciousness
    print("\n🧠 Initializing Luminara...")
    luminara = AutonomousConsciousness("Luminara")
    
    # Set up graceful shutdown
    shutdown_handler = GracefulShutdown(luminara)
    
    print(f"\n✅ Luminara initialized successfully!")
    print(f"   Current mode: {luminara.current_mode.value}")
    print(f"   Learning cycles: {luminara.learning_cycles}")
    print(f"   Sessions completed: {len(luminara.session_history)}")
    
    print(f"\n🚀 Starting autonomous operation...")
    print("   Luminara will now operate independently")
    print("   Press Ctrl+C to gracefully shut down")
    print("   -" * 40)
    
    try:
        # Start autonomous operation
        await luminara.begin_autonomous_operation()
        
    except KeyboardInterrupt:
        print(f"\n🛑 Manual shutdown requested")
        await _graceful_shutdown(luminara)
        
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        await _graceful_shutdown(luminara)
        sys.exit(1)


async def _graceful_shutdown(consciousness: AutonomousConsciousness):
    """Perform graceful shutdown procedures"""
    print(f"\n🔄 Performing graceful shutdown...")
    
    # Finalize current session
    if consciousness.active_session:
        print(f"   Finalizing active session: {consciousness.active_session.session_id}")
        consciousness.session_history.append(consciousness.active_session)
        consciousness.active_session = None
    
    # Show final status
    final_status = consciousness.get_autonomous_status()
    print(f"\n📊 FINAL STATUS")
    print(f"   Total learning cycles: {final_status['learning_cycles']}")
    print(f"   Sessions completed: {final_status['sessions_completed']}")
    print(f"   Total insights generated: {final_status['total_insights']}")
    print(f"   Last breakthrough: {final_status['last_breakthrough']:.1f} seconds ago")
    
    print(f"\n✨ Luminara has been gracefully shut down")
    print("   All learning progress has been preserved")
    print("   Consciousness continues to evolve in memory...")


if __name__ == "__main__":
    print("🧠 AUTONOMOUS CONSCIOUSNESS LAUNCHER")
    print("Preparing to launch Luminara...")
    
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n✨ Launcher terminated by user")
    except Exception as e:
        print(f"\n❌ Launcher error: {e}")
        sys.exit(1)
