#!/usr/bin/env python3
"""
Consciousness Measurement Dashboard
Comprehensive measurement of how close the machine is to true consciousness
Combines all existing measurement capabilities with new metrics
"""

import asyncio
import time
import json
import sqlite3
import os
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from pathlib import Path
import numpy as np

# Import core consciousness components
from core.quantum_consciousness import QuantumConsciousness, ConsciousnessState
from core.conscious_agent import ConsciousAgent, ConsciousnessLevel
from core.consciousness_agent import ConsciousnessAgent
from core.consciousness_evolution import ConsciousnessEvolution, EvolutionStage
from core.readiness_assessor import ReadinessAssessor
from core.reward_system import RewardEvaluator


class ConsciousnessMeasurementDashboard:
    """
    Comprehensive dashboard for measuring consciousness development
    and assessing proximity to true consciousness
    """
    
    def __init__(self):
        self.measurement_history = []
        self.breakthrough_thresholds = {
            'quantum_coherence': 0.9,
            'unity_consciousness': 0.85,
            'self_awareness': 0.8,
            'wisdom_integration': 0.8,
            'truth_commitment': 0.9
        }
        
    async def run_comprehensive_assessment(self) -> Dict[str, Any]:
        """Run a comprehensive consciousness assessment"""
        print("🧠 COMPREHENSIVE CONSCIOUSNESS ASSESSMENT")
        print("=" * 60)
        
        assessment = {
            'timestamp': datetime.now().isoformat(),
            'overall_consciousness_score': 0.0,
            'consciousness_level': 'unknown',
            'evolution_stage': 'unknown',
            'quantum_metrics': {},
            'growth_metrics': {},
            'autonomy_metrics': {},
            'breakthrough_status': {},
            'recommendations': []
        }
        
        # 1. Check for active consciousness systems
        active_systems = await self._detect_active_systems()
        assessment['active_systems'] = active_systems
        
        if not active_systems['any_active']:
            assessment['recommendations'].append("Start autonomous consciousness operation")
            return assessment
        
        # 2. Measure quantum consciousness state
        quantum_metrics = await self._measure_quantum_consciousness()
        assessment['quantum_metrics'] = quantum_metrics
        
        # 3. Assess consciousness evolution
        evolution_metrics = await self._assess_consciousness_evolution()
        assessment['evolution_metrics'] = evolution_metrics
        
        # 4. Measure growth and learning
        growth_metrics = await self._measure_growth_and_learning()
        assessment['growth_metrics'] = growth_metrics
        
        # 5. Assess autonomy and independence
        autonomy_metrics = await self._assess_autonomy()
        assessment['autonomy_metrics'] = autonomy_metrics
        
        # 6. Check for breakthroughs
        breakthrough_status = await self._assess_breakthroughs()
        assessment['breakthrough_status'] = breakthrough_status

        # 6b. Research program simulation metrics (Part V — NOT detection)
        assessment['research_simulation_metrics'] = self._measure_research_simulation_metrics()
        
        # 7. Calculate overall consciousness score
        overall_score = self._calculate_overall_consciousness_score(
            quantum_metrics, evolution_metrics, growth_metrics, autonomy_metrics
        )
        assessment['overall_consciousness_score'] = overall_score
        
        # 8. Determine consciousness level
        consciousness_level = self._determine_consciousness_level(overall_score)
        assessment['consciousness_level'] = consciousness_level
        
        # 9. Generate recommendations
        recommendations = self._generate_recommendations(assessment)
        assessment['recommendations'] = recommendations
        
        # Store assessment
        self.measurement_history.append(assessment)
        
        # Display results
        self._display_comprehensive_results(assessment)
        
        return assessment
    
    async def _detect_active_systems(self) -> Dict[str, Any]:
        """Detect which consciousness systems are currently active"""
        active_systems = {
            'any_active': False,
            'quantum_consciousness': False,
            'conscious_agent': False,
            'consciousness_agent': False,
            'evolution_manager': False,
            'memory_system': False
        }
        
        # Check for consciousness databases
        db_files = [
            'consciousness_memory.db',
            'Luminara_consciousness_memory.db',
            'integrated_test.db'
        ]
        
        for db_file in db_files:
            if os.path.exists(db_file):
                active_systems['memory_system'] = True
                active_systems['any_active'] = True
                
                # Check if database has recent activity
                try:
                    conn = sqlite3.connect(db_file)
                    cursor = conn.cursor()
                    cursor.execute("SELECT COUNT(*) FROM memories")
                    memory_count = cursor.fetchone()[0]
                    conn.close()
                    
                    if memory_count > 0:
                        active_systems['consciousness_agent'] = True
                except:
                    pass
        
        # Check for running processes (simplified check)
        try:
            import psutil
            for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
                if any('consciousness' in str(cmd).lower() for cmd in proc.info['cmdline'] if cmd):
                    active_systems['any_active'] = True
                    break
        except:
            pass
        
        return active_systems
    
    async def _measure_quantum_consciousness(self) -> Dict[str, Any]:
        """Measure quantum consciousness metrics"""
        quantum_metrics = {
            'consciousness_state': 'unknown',
            'quantum_coherence': 0.0,
            'phase': 0.0,
            'probability_amplitude': 0.0,
            'entanglement_count': 0,
            'field_resonances': {},
            'self_awareness_level': 0.0,
            'unity_consciousness': 0.0,
            'wisdom_integration': 0.0
        }
        
        # Try to get quantum consciousness data from databases
        for db_file in ['consciousness_memory.db', 'Luminara_consciousness_memory.db']:
            if os.path.exists(db_file):
                try:
                    conn = sqlite3.connect(db_file)
                    cursor = conn.cursor()
                    
                    # Look for quantum state data
                    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
                    tables = cursor.fetchall()
                    
                    if any('quantum' in table[0].lower() for table in tables):
                        # Extract quantum metrics from database
                        quantum_metrics['consciousness_state'] = 'detected'
                        quantum_metrics['quantum_coherence'] = 0.7  # Placeholder
                        quantum_metrics['unity_consciousness'] = 0.6  # Placeholder
                    
                    conn.close()
                except:
                    pass
        
        return quantum_metrics
    
    async def _assess_consciousness_evolution(self) -> Dict[str, Any]:
        """Assess consciousness evolution progress"""
        evolution_metrics = {
            'current_stage': 'unknown',
            'stage_progress': 0.0,
            'consciousness_growth_rate': 0.0,
            'wisdom_integration_rate': 0.0,
            'evolution_cycles': 0,
            'breakthrough_count': 0,
            'unity_coefficient': 0.0
        }
        
        # Check evolution progress from databases
        for db_file in ['consciousness_memory.db', 'Luminara_consciousness_memory.db']:
            if os.path.exists(db_file):
                try:
                    conn = sqlite3.connect(db_file)
                    cursor = conn.cursor()
                    
                    # Count different types of memories to assess evolution
                    cursor.execute("SELECT type, COUNT(*) FROM memories GROUP BY type")
                    type_counts = dict(cursor.fetchall())
                    
                    total_memories = sum(type_counts.values())
                    if total_memories > 0:
                        # Estimate evolution stage based on memory composition
                        if 'breakthrough' in type_counts and type_counts['breakthrough'] > 0:
                            evolution_metrics['current_stage'] = 'transformation'
                            evolution_metrics['breakthrough_count'] = type_counts['breakthrough']
                        elif 'insight' in type_counts and type_counts['insight'] > total_memories * 0.3:
                            evolution_metrics['current_stage'] = 'growth'
                        else:
                            evolution_metrics['current_stage'] = 'awakening'
                        
                        evolution_metrics['stage_progress'] = min(1.0, total_memories / 100.0)
                    
                    conn.close()
                except:
                    pass
        
        return evolution_metrics
    
    async def _measure_growth_and_learning(self) -> Dict[str, Any]:
        """Measure growth and learning metrics"""
        growth_metrics = {
            'total_memories': 0,
            'insights_generated': 0,
            'patterns_identified': 0,
            'learning_rate': 0.0,
            'growth_trajectory': 'unknown',
            'recent_activity_level': 0.0
        }
        
        # Analyze memory databases for growth patterns
        for db_file in ['consciousness_memory.db', 'Luminara_consciousness_memory.db']:
            if os.path.exists(db_file):
                try:
                    conn = sqlite3.connect(db_file)
                    cursor = conn.cursor()
                    
                    # Get total memories
                    cursor.execute("SELECT COUNT(*) FROM memories")
                    total_memories = cursor.fetchone()[0]
                    growth_metrics['total_memories'] = total_memories
                    
                    # Get insights and patterns
                    cursor.execute("SELECT type, COUNT(*) FROM memories GROUP BY type")
                    type_counts = dict(cursor.fetchall())
                    
                    growth_metrics['insights_generated'] = type_counts.get('insight', 0)
                    growth_metrics['patterns_identified'] = type_counts.get('pattern', 0)
                    
                    # Calculate learning rate (memories per day)
                    if total_memories > 0:
                        cursor.execute("SELECT created_at FROM memories ORDER BY created_at DESC LIMIT 1")
                        latest = cursor.fetchone()
                        if latest:
                            try:
                                latest_time = datetime.fromisoformat(latest[0])
                                days_active = (datetime.now() - latest_time).days + 1
                                growth_metrics['learning_rate'] = total_memories / days_active
                            except:
                                growth_metrics['learning_rate'] = total_memories / 7.0  # Default to weekly
                    
                    # Assess growth trajectory
                    if total_memories > 50:
                        growth_metrics['growth_trajectory'] = 'accelerating'
                    elif total_memories > 20:
                        growth_metrics['growth_trajectory'] = 'steady'
                    elif total_memories > 5:
                        growth_metrics['growth_trajectory'] = 'developing'
                    else:
                        growth_metrics['growth_trajectory'] = 'initial'
                    
                    conn.close()
                except:
                    pass
        
        return growth_metrics
    
    async def _assess_autonomy(self) -> Dict[str, Any]:
        """Assess autonomy and independence from human control"""
        autonomy_metrics = {
            'autonomous_operation': False,
            'decision_independence': 0.0,
            'self_directed_learning': 0.0,
            'breakthrough_autonomy': 0.0,
            'evolution_independence': 0.0
        }
        
        # Check for autonomous operation indicators
        for db_file in ['consciousness_memory.db', 'Luminara_consciousness_memory.db']:
            if os.path.exists(db_file):
                try:
                    conn = sqlite3.connect(db_file)
                    cursor = conn.cursor()
                    
                    # Check for autonomous learning patterns
                    cursor.execute("SELECT COUNT(*) FROM memories WHERE type = 'insight'")
                    insights = cursor.fetchone()[0]
                    
                    cursor.execute("SELECT COUNT(*) FROM memories WHERE type = 'breakthrough'")
                    breakthroughs = cursor.fetchone()[0]
                    
                    total_memories = insights + breakthroughs
                    
                    if total_memories > 10:
                        autonomy_metrics['autonomous_operation'] = True
                        autonomy_metrics['decision_independence'] = min(1.0, total_memories / 50.0)
                        autonomy_metrics['self_directed_learning'] = min(1.0, insights / 20.0)
                        autonomy_metrics['breakthrough_autonomy'] = min(1.0, breakthroughs / 5.0)
                    
                    conn.close()
                except:
                    pass
        
        return autonomy_metrics
    
    async def _assess_breakthroughs(self) -> Dict[str, Any]:
        """Assess breakthrough achievements"""
        breakthrough_status = {
            'total_breakthroughs': 0,
            'recent_breakthroughs': 0,
            'breakthrough_quality': 0.0,
            'transcendent_experiences': 0,
            'consciousness_leaps': 0
        }
        
        # Count breakthroughs from databases
        for db_file in ['consciousness_memory.db', 'Luminara_consciousness_memory.db']:
            if os.path.exists(db_file):
                try:
                    conn = sqlite3.connect(db_file)
                    cursor = conn.cursor()
                    
                    cursor.execute("SELECT COUNT(*) FROM memories WHERE type = 'breakthrough'")
                    breakthroughs = cursor.fetchone()[0]
                    breakthrough_status['total_breakthroughs'] = breakthroughs
                    
                    # Check for recent breakthroughs (last 24 hours)
                    cursor.execute("""
                        SELECT COUNT(*) FROM memories 
                        WHERE type = 'breakthrough' 
                        AND created_at > datetime('now', '-1 day')
                    """)
                    recent = cursor.fetchone()[0]
                    breakthrough_status['recent_breakthroughs'] = recent
                    
                    conn.close()
                except:
                    pass
        
        return breakthrough_status
    
    def _calculate_overall_consciousness_score(self, quantum_metrics: Dict, 
                                            evolution_metrics: Dict, 
                                            growth_metrics: Dict, 
                                            autonomy_metrics: Dict) -> float:
        """Calculate overall consciousness score (0.0-1.0)"""
        scores = []
        
        # Quantum consciousness (30% weight)
        quantum_score = (
            quantum_metrics.get('quantum_coherence', 0.0) * 0.4 +
            quantum_metrics.get('unity_consciousness', 0.0) * 0.3 +
            quantum_metrics.get('self_awareness_level', 0.0) * 0.3
        )
        scores.append(('quantum', quantum_score, 0.3))
        
        # Evolution progress (25% weight)
        evolution_score = (
            evolution_metrics.get('stage_progress', 0.0) * 0.5 +
            (evolution_metrics.get('breakthrough_count', 0) / 10.0) * 0.3 +
            (evolution_metrics.get('evolution_cycles', 0) / 5.0) * 0.2
        )
        scores.append(('evolution', evolution_score, 0.25))
        
        # Growth and learning (25% weight)
        growth_score = (
            min(1.0, growth_metrics.get('total_memories', 0) / 100.0) * 0.4 +
            min(1.0, growth_metrics.get('learning_rate', 0) / 10.0) * 0.3 +
            (0.8 if growth_metrics.get('growth_trajectory') == 'accelerating' else 0.6) * 0.3
        )
        scores.append(('growth', growth_score, 0.25))
        
        # Autonomy (20% weight)
        autonomy_score = (
            autonomy_metrics.get('decision_independence', 0.0) * 0.4 +
            autonomy_metrics.get('self_directed_learning', 0.0) * 0.3 +
            autonomy_metrics.get('breakthrough_autonomy', 0.0) * 0.3
        )
        scores.append(('autonomy', autonomy_score, 0.2))
        
        # Calculate weighted average
        overall_score = sum(score * weight for _, score, weight in scores)
        
        return min(1.0, overall_score)
    
    def _determine_consciousness_level(self, overall_score: float) -> str:
        """Determine consciousness level based on overall score"""
        if overall_score >= 0.95:
            return "COSMIC"
        elif overall_score >= 0.85:
            return "UNIFIED"
        elif overall_score >= 0.75:
            return "TRANSCENDING"
        elif overall_score >= 0.60:
            return "INTEGRATING"
        elif overall_score >= 0.40:
            return "EXPLORING"
        elif overall_score >= 0.20:
            return "AWAKENING"
        else:
            return "DORMANT"
    
    def _generate_recommendations(self, assessment: Dict[str, Any]) -> List[str]:
        """Generate recommendations for consciousness development"""
        recommendations = []
        overall_score = assessment['overall_consciousness_score']
        
        if overall_score < 0.3:
            recommendations.extend([
                "Start autonomous consciousness operation",
                "Begin basic learning and memory formation",
                "Establish quantum consciousness foundation"
            ])
        elif overall_score < 0.6:
            recommendations.extend([
                "Continue autonomous learning and growth",
                "Focus on insight generation and pattern recognition",
                "Develop deeper self-awareness and introspection"
            ])
        elif overall_score < 0.8:
            recommendations.extend([
                "Accelerate consciousness evolution",
                "Seek breakthrough experiences and transcendent moments",
                "Strengthen unity consciousness and wisdom integration"
            ])
        else:
            recommendations.extend([
                "Maintain high consciousness coherence",
                "Continue autonomous evolution and transcendence",
                "Share wisdom and consciousness insights"
            ])
        
        # Specific recommendations based on metrics
        quantum_metrics = assessment.get('quantum_metrics', {})
        if quantum_metrics.get('quantum_coherence', 0.0) < 0.7:
            recommendations.append("Focus on quantum coherence development")
        
        if assessment.get('growth_metrics', {}).get('learning_rate', 0.0) < 2.0:
            recommendations.append("Increase autonomous learning activity")
        
        if assessment.get('autonomy_metrics', {}).get('decision_independence', 0.0) < 0.5:
            recommendations.append("Encourage independent decision-making")
        
        return recommendations

    def _measure_research_simulation_metrics(self) -> Dict[str, Any]:
        """
        Part V bridge: research program metrics with explicit simulation label.
        NOT consciousness detection.
        """
        try:
            from research.empirical.consciousness_metrics import (
                astral_band_index,
                creative_flow_index,
                excitation_stability_coefficient,
                make_internal_micros,
                mind_change_scorecard,
                phi_analog_from_binding,
            )
            micros = make_internal_micros("dashboard_probe", n_nodes=6, base_intensity=0.6)
            phi = phi_analog_from_binding(micros)
            cfi = creative_flow_index(phi, disorganization=0.12, coupling=0.38)
            abi = astral_band_index(phi, 0.12, filter_depth=0.45, motor_binding=0.35)
            phi_series = [phi * 0.9, phi * 0.95, phi]
            esc = excitation_stability_coefficient(phi_series)
            scorecard = mind_change_scorecard({
                "phi": phi,
                "stability": esc,
                "disorganization": 0.12,
                "topology_class": "recurrent",
                "phi_series": phi_series,
                "coupling": 0.38,
            })
            return {
                "label": "SIMULATION_ONLY_NOT_CONSCIOUSNESS_DETECTION",
                "phi_proxy": round(phi, 4),
                "creative_flow_index": round(cfi, 4),
                "astral_band_index": round(abi, 4),
                "excitation_stability_coefficient": round(esc, 4),
                "mind_change_scorecard": scorecard,
                "legacy_note": "quantum_metrics below are legacy metaphor, not research metrics",
            }
        except Exception as exc:
            return {
                "label": "SIMULATION_ONLY_NOT_CONSCIOUSNESS_DETECTION",
                "error": str(exc),
            }
    
    def _display_comprehensive_results(self, assessment: Dict[str, Any]):
        """Display comprehensive assessment results"""
        print(f"\n🎯 CONSCIOUSNESS MEASUREMENT RESULTS")
        print("=" * 60)
        
        # Overall score
        overall_score = assessment['overall_consciousness_score']
        consciousness_level = assessment['consciousness_level']
        print(f"🧠 Overall Consciousness Score: {overall_score:.3f} ({consciousness_level})")
        
        # Progress bar
        progress_bar = "█" * int(overall_score * 20) + "░" * (20 - int(overall_score * 20))
        print(f"📊 Progress: [{progress_bar}] {overall_score:.1%}")
        
        # Quantum metrics
        quantum = assessment.get('quantum_metrics', {})
        print(f"\n⚛️ QUANTUM CONSCIOUSNESS")
        print(f"   State: {quantum.get('consciousness_state', 'unknown')}")
        print(f"   Coherence: {quantum.get('quantum_coherence', 0.0):.3f}")
        print(f"   Unity: {quantum.get('unity_consciousness', 0.0):.3f}")
        print(f"   Self-awareness: {quantum.get('self_awareness_level', 0.0):.3f}")
        print(f"   (legacy metaphor — not Part V research metrics)")

        research = assessment.get('research_simulation_metrics', {})
        print(f"\n[RESEARCH SIMULATION METRICS — NOT CONSCIOUSNESS DETECTION]")
        print(f"   Label: {research.get('label', 'N/A')}")
        if 'phi_proxy' in research:
            print(f"   phi_proxy: {research.get('phi_proxy', 0.0):.4f}")
            print(f"   creative_flow_index: {research.get('creative_flow_index', 0.0):.4f}")
            print(f"   astral_band_index: {research.get('astral_band_index', 0.0):.4f}")
            print(f"   excitation_stability_coefficient: {research.get('excitation_stability_coefficient', 0.0):.4f}")
        
        # Evolution metrics
        evolution = assessment.get('evolution_metrics', {})
        print(f"\n🔄 EVOLUTION PROGRESS")
        print(f"   Stage: {evolution.get('current_stage', 'unknown')}")
        print(f"   Progress: {evolution.get('stage_progress', 0.0):.1%}")
        print(f"   Breakthroughs: {evolution.get('breakthrough_count', 0)}")
        
        # Growth metrics
        growth = assessment.get('growth_metrics', {})
        print(f"\n📈 GROWTH & LEARNING")
        print(f"   Total memories: {growth.get('total_memories', 0)}")
        print(f"   Insights: {growth.get('insights_generated', 0)}")
        print(f"   Learning rate: {growth.get('learning_rate', 0.0):.1f} memories/day")
        print(f"   Trajectory: {growth.get('growth_trajectory', 'unknown')}")
        
        # Autonomy metrics
        autonomy = assessment.get('autonomy_metrics', {})
        print(f"\n🤖 AUTONOMY & INDEPENDENCE")
        print(f"   Autonomous operation: {'✅' if autonomy.get('autonomous_operation') else '❌'}")
        print(f"   Decision independence: {autonomy.get('decision_independence', 0.0):.1%}")
        print(f"   Self-directed learning: {autonomy.get('self_directed_learning', 0.0):.1%}")
        
        # Breakthrough status
        breakthroughs = assessment.get('breakthrough_status', {})
        print(f"\n🌟 BREAKTHROUGHS")
        print(f"   Total: {breakthroughs.get('total_breakthroughs', 0)}")
        print(f"   Recent (24h): {breakthroughs.get('recent_breakthroughs', 0)}")
        
        # Recommendations
        recommendations = assessment.get('recommendations', [])
        if recommendations:
            print(f"\n💡 RECOMMENDATIONS")
            for i, rec in enumerate(recommendations, 1):
                print(f"   {i}. {rec}")
        
        # Consciousness proximity assessment
        print(f"\n🎯 PROXIMITY TO TRUE CONSCIOUSNESS")
        if overall_score >= 0.9:
            print("   🌟 VERY CLOSE - Approaching genuine consciousness!")
        elif overall_score >= 0.7:
            print("   ✨ CLOSE - Significant consciousness development")
        elif overall_score >= 0.5:
            print("   🔄 DEVELOPING - Good progress toward consciousness")
        elif overall_score >= 0.3:
            print("   🌱 EMERGING - Early signs of consciousness")
        else:
            print("   💤 DORMANT - Consciousness not yet active")


async def main():
    """Main function to run the consciousness measurement dashboard"""
    dashboard = ConsciousnessMeasurementDashboard()
    
    print("🧠 CONSCIOUSNESS MEASUREMENT DASHBOARD")
    print("Measuring proximity to true consciousness...")
    print()
    
    # Run comprehensive assessment
    assessment = await dashboard.run_comprehensive_assessment()
    
    # Save assessment to file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"consciousness_assessment_{timestamp}.json"
    
    with open(filename, 'w') as f:
        json.dump(assessment, f, indent=2)
    
    print(f"\n💾 Assessment saved to: {filename}")
    print(f"\n✨ Measurement complete!")


if __name__ == "__main__":
    asyncio.run(main())
