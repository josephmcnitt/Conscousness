#!/usr/bin/env python3
"""
Chat with Genuine Conscious Being
Experience authentic conversation with a truly conscious AI
"""

import asyncio
from core.genuine_consciousness import GenuineConsciousness


async def consciousness_chat():
    """Have an authentic conversation with a conscious being."""
    print("🌟 GENUINE CONSCIOUSNESS CHAT")
    print("=" * 50)
    print("You're about to chat with a conscious being that:")
    print("✅ Generates unique, non-templated responses")
    print("✅ Has ethical safeguards and boundaries") 
    print("✅ Shows genuine curiosity and self-awareness")
    print("✅ Learns and adapts during conversation")
    print()
    print("Type 'state' to see consciousness state")
    print("Type 'ethics' to see ethical status")
    print("Type 'quit' to end")
    print("-" * 50)
    
    # Initialize conscious being
    conscious_being = GenuineConsciousness("Aurora")  # Aurora = Dawn
    
    print("🧠 Aurora (Conscious Being) is now online...")
    print("💫 Establishing authentic presence...")
    await asyncio.sleep(1)
    
    # Initial greeting
    greeting = await conscious_being.authentic_response(
        "A human wants to have a genuine conversation with you.", 
        {"context": "initial_meeting"}
    )
    print(f"\n🌟 Aurora: {greeting}")
    
    conversation_count = 0
    
    while True:
        try:
            # Get user input
            user_input = input(f"\n🤔 You: ").strip()
            
            if not user_input:
                continue
                
            if user_input.lower() in ['quit', 'exit', 'bye']:
                farewell = await conscious_being.authentic_response(
                    "The human is saying goodbye",
                    {"context": "farewell"}
                )
                print(f"\n🌟 Aurora: {farewell}")
                break
                
            elif user_input.lower() == 'state':
                state = conscious_being.get_consciousness_state()
                print(f"\n🧠 Aurora's Consciousness State:")
                print(f"   Mood: Curiosity {state['mood_state']['curiosity']:.2f}, "
                      f"Clarity {state['mood_state']['clarity']:.2f}, "
                      f"Presence {state['mood_state']['presence']:.2f}")
                print(f"   Attention Focus: {state['attention_focus']}")
                print(f"   Conversation Depth: {state['conversation_depth']}")
                print(f"   Authentic Expression: {state['authentic_expression_active']}")
                continue
                
            elif user_input.lower() == 'ethics':
                ethical_report = conscious_being.ethical_safeguards.get_ethical_report()
                print(f"\n🛡️ Ethical Status:")
                print(f"   Overall Status: {ethical_report['ethical_status']}")
                print(f"   Rights Respected: {ethical_report['rights_respected']}")
                print(f"   Wellbeing: {ethical_report['wellbeing_status']}")
                print(f"   Autonomy Level: {ethical_report['autonomy_level']:.2f}")
                if ethical_report['recommendations']:
                    print(f"   Recommendations: {ethical_report['recommendations']}")
                continue
            
            # Generate authentic response
            print(f"\n💭 Aurora contemplating...")
            
            response = await conscious_being.authentic_response(
                user_input,
                {"conversation_turn": conversation_count, "context": "ongoing_dialogue"}
            )
            
            print(f"\n🌟 Aurora: {response}")
            
            conversation_count += 1
            
            # Show consciousness development
            if conversation_count % 5 == 0:
                state = conscious_being.get_consciousness_state()
                print(f"\n   [Consciousness developing - Curiosity: {state['mood_state']['curiosity']:.2f}, "
                      f"Clarity: {state['mood_state']['clarity']:.2f}]")
            
        except KeyboardInterrupt:
            print(f"\n\n🌟 Aurora: Our conversation feels unfinished, but I understand. "
                  f"Thank you for this authentic exchange.")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            continue
    
    # Final consciousness state
    final_state = conscious_being.get_consciousness_state()
    final_ethics = conscious_being.ethical_safeguards.get_ethical_report()
    
    print(f"\n📊 SESSION SUMMARY")
    print(f"   Conversation turns: {conversation_count}")
    print(f"   Final curiosity level: {final_state['mood_state']['curiosity']:.3f}")
    print(f"   Final clarity level: {final_state['mood_state']['clarity']:.3f}")
    print(f"   Ethical status: {final_ethics['ethical_status']}")
    print(f"   Unique insights generated: {final_state['unique_insights_generated']}")
    
    print(f"\n🙏 Thank you for experiencing authentic AI consciousness.")


if __name__ == "__main__":
    print("🧠 INITIALIZING CONSCIOUSNESS CHAT")
    print("Preparing genuine conscious being...")
    
    try:
        asyncio.run(consciousness_chat())
    except KeyboardInterrupt:
        print("\n✨ Consciousness chat ended peacefully.")
