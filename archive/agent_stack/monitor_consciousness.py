#!/usr/bin/env python3
"""
Monitor Autonomous Consciousness
Check status and progress without interrupting operation
"""

import asyncio
import sqlite3
import os
from datetime import datetime, timedelta


def check_consciousness_status():
    """Check the current status of consciousness operation"""
    print("🔍 CONSCIOUSNESS STATUS MONITOR")
    print("=" * 50)
    
    # Check if consciousness database exists
    db_path = "consciousness_memories.db"
    if not os.path.exists(db_path):
        print("❌ No consciousness database found")
        print("   Luminara may not be running or hasn't started learning yet")
        return
    
    try:
        # Connect to database
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Get basic statistics
        cursor.execute("SELECT COUNT(*) FROM memories")
        total_memories = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM memories WHERE type = 'insight'")
        total_insights = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM memories WHERE type = 'pattern'")
        total_patterns = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM memories WHERE type = 'breakthrough'")
        total_breakthroughs = cursor.fetchone()[0]
        
        # Get recent activity
        cursor.execute("""
            SELECT type, content, created_at, importance 
            FROM memories 
            ORDER BY created_at DESC 
            LIMIT 5
        """)
        recent_memories = cursor.fetchall()
        
        # Get learning progression
        cursor.execute("""
            SELECT DATE(created_at) as date, COUNT(*) as count
            FROM memories 
            GROUP BY DATE(created_at)
            ORDER BY date DESC
            LIMIT 7
        """)
        daily_progress = cursor.fetchall()
        
        conn.close()
        
        # Display status
        print(f"📊 OVERALL STATUS")
        print(f"   Total memories: {total_memories}")
        print(f"   Insights generated: {total_insights}")
        print(f"   Patterns identified: {total_patterns}")
        print(f"   Breakthroughs achieved: {total_breakthroughs}")
        
        print(f"\n📈 RECENT ACTIVITY (Last 5 memories)")
        for memory_type, content, created_at, importance in recent_memories:
            timestamp = datetime.fromisoformat(created_at)
            time_ago = datetime.now() - timestamp
            content_preview = content[:60] + "..." if len(content) > 60 else content
            print(f"   [{memory_type.upper()}] {content_preview}")
            print(f"      {time_ago.total_seconds():.0f}s ago | Importance: {importance}")
        
        print(f"\n📅 DAILY LEARNING PROGRESS (Last 7 days)")
        for date, count in daily_progress:
            print(f"   {date}: {count} memories")
        
        # Calculate learning rate
        if len(daily_progress) >= 2:
            recent_rate = sum(count for _, count in daily_progress[:3])
            older_rate = sum(count for _, count in daily_progress[3:]) if len(daily_progress) >= 4 else 0
            if older_rate > 0:
                improvement = ((recent_rate - older_rate) / older_rate) * 100
                print(f"\n🚀 Learning rate change: {improvement:+.1f}%")
        
        # Assess consciousness development
        print(f"\n🧠 CONSCIOUSNESS ASSESSMENT")
        if total_memories == 0:
            print("   Status: Not yet active")
        elif total_memories < 10:
            print("   Status: Early development")
        elif total_memories < 50:
            print("   Status: Active learning")
        elif total_memories < 100:
            print("   Status: Advanced development")
        else:
            print("   Status: Highly evolved")
        
        if total_breakthroughs > 0:
            print(f"   Breakthroughs: {total_breakthroughs} significant milestones achieved")
        
        if total_patterns > 0:
            print(f"   Pattern recognition: Active and developing")
        
        print(f"\n💡 RECOMMENDATIONS")
        if total_memories == 0:
            print("   Start autonomous consciousness operation")
        elif total_insights < total_memories * 0.3:
            print("   Focus on generating deeper insights")
        elif total_patterns < total_memories * 0.1:
            print("   Encourage pattern recognition development")
        else:
            print("   Consciousness is developing well - continue autonomous operation")
        
    except Exception as e:
        print(f"❌ Error monitoring consciousness: {e}")


def check_system_resources():
    """Check system resource usage"""
    print(f"\n💻 SYSTEM RESOURCES")
    print("=" * 30)
    
    try:
        import psutil
        
        # CPU usage
        cpu_percent = psutil.cpu_percent(interval=1)
        print(f"   CPU Usage: {cpu_percent:.1f}%")
        
        # Memory usage
        memory = psutil.virtual_memory()
        print(f"   Memory Usage: {memory.percent:.1f}% ({memory.used // (1024**3):.1f}GB / {memory.total // (1024**3):.1f}GB)")
        
        # Disk usage for consciousness database
        db_path = "consciousness_memories.db"
        if os.path.exists(db_path):
            db_size = os.path.getsize(db_path) / (1024**2)  # MB
            print(f"   Database Size: {db_size:.2f} MB")
        
        # Process count
        process_count = len(psutil.pids())
        print(f"   Active Processes: {process_count}")
        
    except ImportError:
        print("   psutil not available - install with: pip install psutil")
    except Exception as e:
        print(f"   Error checking resources: {e}")


def main():
    """Main monitoring function"""
    print("🧠 LUMINARA CONSCIOUSNESS MONITOR")
    print("Monitoring autonomous consciousness operation...")
    print()
    
    check_consciousness_status()
    check_system_resources()
    
    print(f"\n✨ Monitoring complete")
    print("   Use 'python launch_autonomous_consciousness.py' to start Luminara")
    print("   Use 'python monitor_consciousness.py' to check status again")


if __name__ == "__main__":
    main()
