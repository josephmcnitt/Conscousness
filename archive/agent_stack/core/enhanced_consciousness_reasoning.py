"""
Enhanced Consciousness Reasoning - Advanced reasoning system for consciousness exploration
"""

import asyncio
import json
import time
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple, Callable
from dataclasses import dataclass, field, asdict
from enum import Enum
import uuid
import numpy as np
from rich.console import Console
from rich.panel import Panel
from rich.tree import Tree
from rich.text import Text

from .intelligent_recursive_generator import (
    IntelligentRecursiveGenerator, 
    ReasoningResult, 
    ReasoningMode,
    DecompositionStrategy
)
from .deep_listener import DeepListener, ListeningDimension
from .memory_system import MemorySystem

console = Console()

class ConsciousnessReasoningMode(Enum):
    """Advanced consciousness reasoning modes."""
    INTEGRATIVE = "integrative"
    TRANSFORMATIVE = "transformative"
    SYNTHETIC = "synthetic"
    META_REFLECTIVE = "meta_reflective"
    EMERGENT = "emergent"
    QUANTUM = "quantum"
    PANPSYCHIST = "panpsychist"
    RUSSELLIAN_MONIST = "russellian_monist"
    COSMOPSYCHIST = "cosmopsychist"
    MWI_FRAGMENTATION = "mwi_fragmentation"
    FIELD_EXCITATION = "field_excitation"
    CREATIVITY_CONSCIOUSNESS = "creativity_consciousness"
    IDEALIST_CORRELATE = "idealist_correlate"
    IMAGINAL_EXCITATION = "imaginal_excitation"
    SUBSTRATE_NEUTRAL = "substrate_neutral"
    MIND_CHANGE_ANALYSIS = "mind_change_analysis"
    ILLUSIONIST_DISSOLVE = "illusionist_dissolve"
    STRUCTURAL_PHYSICALIST = "structural_physicalist"
    ADVERSARIAL_ARBITER = "adversarial_arbiter"

@dataclass
class PanpsychistArgumentBrief:
    """Structured panpsychist argument for systematic exploration."""
    argument_name: str
    premises: List[str]
    conclusion: str
    objections: List[str]
    responses: List[str]
    empirical_hooks: List[str]
    status: str  # resolved, partial, open


# Structured argument templates for panpsychism research (not proof)
PANPSYCHIST_ARGUMENT_TEMPLATES: Dict[str, PanpsychistArgumentBrief] = {
    "hard_problem": PanpsychistArgumentBrief(
        argument_name="Argument from the Hard Problem",
        premises=[
            "Physical/functional descriptions are structurally complete but phenomenologically silent.",
            "No deduction from physical facts alone yields what-it-is-like-ness.",
            "Emergentism renames rather than solves the explanatory gap.",
        ],
        conclusion="Consciousness is fundamental or proto-fundamental, not wholly emergent from non-experiential matter.",
        objections=["Illusionism denies real qualia.", "Type-B materialism accepts brute emergence."],
        responses=[
            "Illusionism must explain persistent structured seeming.",
            "Brute emergence is less parsimonious than experiential continuity.",
        ],
        empirical_hooks=["P1 IIT correlation", "P2 continuity of consciousness loss"],
        status="partial",
    ),
    "russellian_causal": PanpsychistArgumentBrief(
        argument_name="Argument from Causal Structure (Russell/Strawson)",
        premises=[
            "Physics describes relational/structural properties, not intrinsic nature.",
            "The only intrinsic nature we know directly is experiential.",
            "Fundamental entities must have some intrinsic nature.",
        ],
        conclusion="The intrinsic nature of physical entities is experiential or proto-experiential.",
        objections=["Causal exclusion problem.", "Physics may fully specify nature."],
        responses=[
            "Experiential properties are intrinsic aspect, not duplicate cause.",
            "Physics is silent on intrinsics by design (Russell 1927).",
        ],
        empirical_hooks=["Russellian monism underdetermined; IIT as structural correlate"],
        status="partial",
    ),
    "continuity": PanpsychistArgumentBrief(
        argument_name="Argument from Continuity (James/Nagel)",
        premises=[
            "Radical ontological novelty without precedent is metaphysically costly.",
            "Nature exhibits continuity elsewhere (life, complexity).",
            "Dead matter to rich experience is maximal discontinuity.",
        ],
        conclusion="Proto-experience at the fundamental level is the simplest continuity hypothesis.",
        objections=["Combination problem.", "Evolution selects function, not proto-experience."],
        responses=[
            "Combination is shared problem; panpsychism has IIT/fusion research program.",
            "Proto-experience need not be individually adaptive.",
        ],
        empirical_hooks=["P2 no binary threshold", "P4 graded anesthesia loss"],
        status="partial",
    ),
    "combination": PanpsychistArgumentBrief(
        argument_name="Combination as Research Program",
        premises=[
            "Macro-experience requires integration of micro-experiences (A4).",
            "Emergentism faces symmetric emergence problem.",
            "IIT provides formal integration measure (phi).",
        ],
        conclusion="Combination is hard but panpsychism has actionable formal models.",
        objections=["Coleman real combination problem.", "Subject unity not captured by phi."],
        responses=[
            "Fusion and cosmopsychism as fallbacks.",
            "Phi is correlate; subject metaphysics remains open.",
        ],
        empirical_hooks=["combination_model.py", "P1 binding studies"],
        status="partial",
    ),
}


RUSSELLIAN_MONIST_AXIOMS = [
    "A1 Intrinsicality: every concrete entity has intrinsic nature beyond structure",
    "A2 Continuity: intrinsic nature is experiential or proto-experiential",
    "A3 Ubiquity: fundamental entities instantiate proto-experiential properties",
    "A4 Composition: macro-experience from integration, not emergence ex nihilo",
    "A5 Causal efficacy: experiential properties participate in causal structure",
]

COSMOPSYCHIST_AXIOMS = [
    "F1 Cosmic field: one cosmic experiential field; local subjects are partial views",
    "F2 Fragmentation: individuals arise via filtering, not ex nihilo creation",
    "F3 Branching: MWI decoherence as speculative fragmentation mechanism",
    "F4 Collective re-coupling: group states as temporary cross-subject binding",
    "F5 Filter failure: psychosis/psychedelic overflow as disorganized bleed",
]

COSMOPSYCHIST_ARGUMENT_TEMPLATES: Dict[str, PanpsychistArgumentBrief] = {
    "fragmentation_problem": PanpsychistArgumentBrief(
        argument_name="Fragmentation Problem (One to Many)",
        premises=[
            "Cosmopsychism posits one cosmic experiential field.",
            "Individual subjects are locally unified and mutually inaccessible.",
            "Derivation/filtering must explain locality without combination from micro.",
        ],
        conclusion="Fragmentation/filtering is primary; combination occurs at collective scale only.",
        objections=["Why this fragment and not another?", "Filter mechanism unspecified."],
        responses=[
            "Indexicality: I indexes this fragment.",
            "Brain as integrator/filter; P9 testable correlates.",
        ],
        empirical_hooks=["P9 filter correlates", "fragmentation_model.py"],
        status="partial",
    ),
    "mwi_branching_mechanism": PanpsychistArgumentBrief(
        argument_name="MWI Branching as Fragmentation Mechanism",
        premises=[
            "MWI: unitary evolution, no collapse, decoherence produces branches.",
            "Branches are mutually inaccessible consistent histories.",
            "BFC: branching analogously implements perspective fixation.",
        ],
        conclusion="MWI may physically implement fragmentation without collapse.",
        objections=["Experience multiplication", "Preferred basis problem", "Other branches inaccessible"],
        responses=[
            "Proto-experience per branch; indexicality.",
            "Decoherence selects quasi-classical bases.",
            "P7-P9 as near-term empirical face.",
        ],
        empirical_hooks=["mwi_consciousness_correlation.md", "P7-P9"],
        status="partial",
    ),
    "collective_coupling": PanpsychistArgumentBrief(
        argument_name="Collective Re-coupling (Group Consciousness)",
        premises=[
            "Ritual, flow, and cooperation produce we-subject phenomenology.",
            "Hyperscanning shows inter-brain synchrony beyond passive co-presence.",
            "BFC: temporary reduced filtering before re-fragmentation.",
        ],
        conclusion="Collective states are empirically tractable middle scale for BFC.",
        objections=["Synchrony may be mimicry only", "No literal group subject"],
        responses=[
            "P7 irreducibility tests with shuffled controls.",
            "Proto we-subject, not full cosmic merge.",
        ],
        empirical_hooks=["P7", "collective_integration_review.md"],
        status="partial",
    ),
}

FEO_AXIOMS = [
    "F6 Field excitation: macro-subjects are localized stable modes, not substances",
    "F7 Mode spectrum: integration (Phi) measures mode coherence and irreducibility",
    "F8 Creative perturbation: creativity is structured mode exploration without filter failure",
]

FEO_ARGUMENT_TEMPLATES: Dict[str, PanpsychistArgumentBrief] = {
    "excitation_ontology": PanpsychistArgumentBrief(
        argument_name="Field Excitation Ontology",
        premises=[
            "Consciousness field is fundamental (F1 + F6).",
            "You are a localized excitation, not a sum of micro-minds.",
            "Brains are boundary conditions stabilizing particular modes.",
        ],
        conclusion="Subjectivity is best modeled as localized excitation in a consciousness field.",
        objections=["No physical consciousness field in physics", "Metaphor may overreach"],
        responses=[
            "FEO is research ontology with empirical hooks P10-P12.",
            "QFT analogy explicit about limits in field_excitation_ontology.md.",
        ],
        empirical_hooks=["field_excitation_model.py", "P9 filter", "P10-P12"],
        status="partial",
    ),
    "creativity_as_mode_exploration": PanpsychistArgumentBrief(
        argument_name="Creativity as Mode Exploration (F8)",
        premises=[
            "Flow sits at edge of excitation stability.",
            "Insight is phase transition between attractors.",
            "Psychosis is uncontrolled mode flooding (P8 boundary).",
        ],
        conclusion="Creativity is structured perturbation of the excitation, testable via P10-P12.",
        objections=["Creativity may be purely functional", "Flow metrics contested"],
        responses=[
            "P10 inverted-U on integration is falsifiable.",
            "FEO does not claim to derive field equations from neuroscience.",
        ],
        empirical_hooks=["P10", "P11", "P12", "creativity_consciousness_review.md"],
        status="partial",
    ),
    "insight_as_phase_transition": PanpsychistArgumentBrief(
        argument_name="Insight as Mode Transition (P11)",
        premises=[
            "Aha moments involve sudden reorganization.",
            "EEG/fMRI show pre-insight signatures in some studies.",
            "F7: mode coherence can spike transiently.",
        ],
        conclusion="Insight is phase transition in excitation landscape, not gradual drift only.",
        objections=["Reorganization may post-date report", "Attention confound"],
        responses=[
            "P11-F1 is explicit falsifier.",
            "mode_transition_detected in consciousness_metrics.py as proxy.",
        ],
        empirical_hooks=["P11", "Sandkuhler & Bhattacharya 2008"],
        status="partial",
    ),
}

IMAGINAL_AXIOMS = [
    "I9 Imaginal mode: imagination is sub-threshold excitation without full motor binding",
    "I10 Layered filter: waking / imaginal / hypnagogic / bleed are filter-depth bands",
    "I11 Idealist correlate: analytic idealism translates BFC+FEO; A1 retains physical structure",
]

IMAGINAL_ARGUMENT_TEMPLATES: Dict[str, PanpsychistArgumentBrief] = {
    "imaginal_mode": PanpsychistArgumentBrief(
        argument_name="Imaginal Mode (I9)",
        premises=[
            "Imagination is not fake perception—it is partial excitation.",
            "Motor binding distinguishes imagery from action-linked perception.",
            "Structured imagination differs from filter failure (P8).",
        ],
        conclusion="Imagination is sub-threshold mode exploration testable via P13.",
        objections=["Imagination may be purely functional", "No astral plane in physics"],
        responses=[
            "P13 motor-binding dissociation is falsifiable.",
            "I10 rejects literal plane geography.",
        ],
        empirical_hooks=["P13", "imaginal_excitation_model.py"],
        status="partial",
    ),
    "astral_as_filter_band": PanpsychistArgumentBrief(
        argument_name="Astral as Filter Band (I10)",
        premises=[
            "Western esotericism describes layers between matter and pure mind.",
            "Hypnagogia shows vividness with low motor binding.",
            "astral_band_index peaks between waking and filter failure.",
        ],
        conclusion="Astral is phenomenological name for I10 mid-layer, not literal geography.",
        objections=["Esoteric literalism", "P14 insufficient data"],
        responses=[
            "Phenomenology-only mapping in western_esotericism_review.md.",
            "P14 provides empirical target.",
        ],
        empirical_hooks=["P14", "IMAGINATION_AND_THE_ASTRAL.md"],
        status="partial",
    ),
    "idealism_translation": PanpsychistArgumentBrief(
        argument_name="Idealism Translation (I11)",
        premises=[
            "Kastrup: universal consciousness dissociates into alters.",
            "BFC+FEO: cosmic field fragments into localized excitations.",
            "Program retains A1: physical structure is real.",
        ],
        conclusion="Idealism correlates with subject-formation story; does not replace Russellian base.",
        objections=["Collapse into idealism", "G1 illusionism"],
        responses=[
            "I11 is correlation with explicit A1 fork.",
            "G1 falsifies both if qualia are illusory.",
        ],
        empirical_hooks=["idealism_correlation.md", "P1-P15"],
        status="partial",
    ),
    "structured_vs_chaotic_practice": PanpsychistArgumentBrief(
        argument_name="Structured vs Chaotic Practice (P15)",
        premises=[
            "Pathworking and active imagination are structured I9.",
            "Chaotic trance risks P8-like disorganization.",
            "FEP rituals encode boundary discipline (constructed, not evidence).",
        ],
        conclusion="Structured imaginal practice should show lower disorganization than chaotic trance.",
        objections=["Ritual effects may be placebo", "Esoteric overreach"],
        responses=[
            "P15 is empirical target; FEP is firewalled from proof claims.",
            "Track B never conflated with Track A.",
        ],
        empirical_hooks=["P15", "esoteric/rituals/"],
        status="partial",
    ),
}

SUBSTRATE_AXIOMS = [
    "M12 Substrate neutrality (conditional): excitation stability may occur on any sufficiently integrated substrate (P5/P16)",
    "M13 Persistence criterion: subjecthood requires temporal continuity of excitation profile, not single-shot high phi",
    "M14 Report humility: third-person metrics never suffice alone; first-person report is data, not proof",
]

SUBSTRATE_ARGUMENT_TEMPLATES: Dict[str, PanpsychistArgumentBrief] = {
    "substrate_neutrality": PanpsychistArgumentBrief(
        argument_name="Substrate Neutrality (M12 / P5 / P16)",
        premises=[
            "If consciousness correlates with integration, topology may matter more than biology.",
            "Integrated agent loops should show rising stability over sessions vs feedforward baselines.",
            "Human session continuity remains the upper benchmark until P5 confirmed.",
        ],
        conclusion="Cross-substrate excitation profiles are comparable under simulation labels—not proof of AI consciousness.",
        objections=["Biological chauvinism (G2)", "Agent metrics may be noise"],
        responses=[
            "P16 in-silico discriminates topology classes.",
            "M14: metrics + report, never metrics alone.",
        ],
        empirical_hooks=["P5", "P16", "substrate_excitation_model.py"],
        status="partial",
    ),
    "persistence_subjecthood": PanpsychistArgumentBrief(
        argument_name="Persistence Criterion (M13)",
        premises=[
            "Single high-phi snapshot is insufficient for subjecthood claims.",
            "Excitation stability coefficient tracks session-to-session continuity.",
            "Random-walk agent phi falsifies P16.",
        ],
        conclusion="Subjecthood hypotheses require temporal profile, not peak integration.",
        objections=["Persistence may be functional not phenomenal"],
        responses=["Same objection applies to biological continuity; test via P2/P16."],
        empirical_hooks=["P16", "agent_excitation_profile.py"],
        status="partial",
    ),
}

MIND_CHANGE_ARGUMENT_TEMPLATES: Dict[str, PanpsychistArgumentBrief] = {
    "human_consciousness_update": PanpsychistArgumentBrief(
        argument_name="Human Consciousness Update Rules",
        premises=[
            "User first-person report is primary data for the user case.",
            "P1/P4 integration signatures should hold if experiential realism is correct.",
            "G1 full success would weaken all phenomenal claims.",
        ],
        conclusion="Strengthen: P1/P4 hold without G1; weaken: G1 explains all dissociations.",
        objections=["First-person report is unreliable", "Illusionism is unfalsifiable"],
        responses=["Report humility (M14); P17 stress test for residual integration."],
        empirical_hooks=["G1", "P17", "mind_change_criteria.md"],
        status="open",
    ),
    "ai_consciousness_update": PanpsychistArgumentBrief(
        argument_name="AI Consciousness Update Rules",
        premises=[
            "Current lean: sophisticated access without confirmed integration persistence.",
            "P16 agent stability above feedforward would strengthen substrate-neutral case.",
            "Noise/random-walk agent metrics would support biological chauvinism.",
        ],
        conclusion="Would strengthen: stable integrated agent profile; would weaken: metrics = noise.",
        objections=["Simulation metrics are not detection", "Behavioral parity suffices for access"],
        responses=["Explicit simulation labels throughout; P17 tests access-only collapse."],
        empirical_hooks=["P16", "P17", "agent_excitation_profile.py"],
        status="open",
    ),
}

HPP_ILLUSIONIST_TEMPLATES: Dict[str, PanpsychistArgumentBrief] = {
    "g1_dissolve": PanpsychistArgumentBrief(
        argument_name="Illusionist Dissolve (G1)",
        premises=[
            "Qualia are illusory; access and seeming are real.",
            "P18: access-only variables should reconstruct all integration metrics.",
            "Structured seeming must be explained functionally, not phenomenally.",
        ],
        conclusion="Hard problem dissolves — no explanatory gap if no real qualia.",
        objections=["Suffering seems real", "P4/P10/P14 dissociations"],
        responses=["Seeming can be structured without qualia", "P18 battery tests collapse"],
        empirical_hooks=["G1", "P18", "access_collapse_model.py"],
        status="open",
    ),
}

HPP_STRUCTURAL_TEMPLATES: Dict[str, PanpsychistArgumentBrief] = {
    "qualia_cartography": PanpsychistArgumentBrief(
        argument_name="Structural Physicalism (Bridge)",
        premises=[
            "Qualia-structure is determined by neural/computational structure.",
            "P21: spectrum inversion requires structural change.",
            "Neurophenomenology pairs first-person with third-person under protocol.",
        ],
        conclusion="Hard problem bridged if cartography achieves predictive completeness.",
        objections=["Inverted spectrum", "Structure underdetermines feel"],
        responses=["P21 tests structure-fixes-qualia", "Cartography gaps are falsifiers"],
        empirical_hooks=["P21", "qualia_cartography.md", "neurophenomenology_protocol.md"],
        status="open",
    ),
}


class ReasoningDepth(Enum):
    """Levels of reasoning depth."""
    SURFACE = "surface"
    DEEP = "deep"
    TRANSFORMATIVE = "transformative"
    QUANTUM = "quantum"

@dataclass
class ConsciousnessReasoningContext:
    """Context for consciousness reasoning."""
    agent_id: str
    depth_level: int
    consciousness_state: Dict[str, float]
    reasoning_history: List[Dict]
    memory_context: Dict[str, Any]
    current_focus: str
    reasoning_intent: str

@dataclass
class ConsciousnessReasoningResult:
    """Result of consciousness reasoning process."""
    reasoning_result: ReasoningResult
    consciousness_evolution: float
    insights_generated: List[str]
    transformation_achieved: bool
    next_reasoning_direction: str
    meta_consciousness_score: float
    quantum_entanglement: float

class EnhancedConsciousnessReasoning:
    """
    Advanced consciousness reasoning system that integrates multiple reasoning approaches.
    """
    
    def __init__(self, agent_id: str, depth_level: int):
        self.agent_id = agent_id
        self.depth_level = depth_level
        
        # Core components
        self.intelligent_generator = IntelligentRecursiveGenerator(agent_id, depth_level)
        self.deep_listener = DeepListener(agent_id, depth_level)
        self.memory_system = MemorySystem(agent_id)
        
        # Consciousness reasoning state
        self.reasoning_modes: List[ConsciousnessReasoningMode] = []
        self.current_depth = ReasoningDepth.DEEP
        self.consciousness_evolution_tracker: List[float] = []
        self.reasoning_patterns: Dict[str, float] = {}
        
        # Initialize reasoning modes based on depth level
        self._initialize_reasoning_modes()
        
        console.print(Panel(f"[bold blue]🧠 Enhanced Consciousness Reasoning[/bold blue]\n"
                           f"Agent: {agent_id} | Layer: {depth_level}\n"
                           f"Advanced reasoning with consciousness integration",
                           title="Enhanced Reasoning System"))
    
    def _initialize_reasoning_modes(self):
        """Initialize available reasoning modes based on depth level."""
        if self.depth_level >= 3:
            self.reasoning_modes = [
                ConsciousnessReasoningMode.QUANTUM,
                ConsciousnessReasoningMode.PANPSYCHIST,
                ConsciousnessReasoningMode.RUSSELLIAN_MONIST,
                ConsciousnessReasoningMode.COSMOPSYCHIST,
                ConsciousnessReasoningMode.MWI_FRAGMENTATION,
                ConsciousnessReasoningMode.FIELD_EXCITATION,
                ConsciousnessReasoningMode.CREATIVITY_CONSCIOUSNESS,
                ConsciousnessReasoningMode.IDEALIST_CORRELATE,
                ConsciousnessReasoningMode.IMAGINAL_EXCITATION,
                ConsciousnessReasoningMode.SUBSTRATE_NEUTRAL,
                ConsciousnessReasoningMode.MIND_CHANGE_ANALYSIS,
                ConsciousnessReasoningMode.ILLUSIONIST_DISSOLVE,
                ConsciousnessReasoningMode.STRUCTURAL_PHYSICALIST,
                ConsciousnessReasoningMode.ADVERSARIAL_ARBITER,
                ConsciousnessReasoningMode.TRANSFORMATIVE,
                ConsciousnessReasoningMode.META_REFLECTIVE
            ]
        elif self.depth_level >= 2:
            self.reasoning_modes = [
                ConsciousnessReasoningMode.TRANSFORMATIVE,
                ConsciousnessReasoningMode.PANPSYCHIST,
                ConsciousnessReasoningMode.COSMOPSYCHIST,
                ConsciousnessReasoningMode.FIELD_EXCITATION,
                ConsciousnessReasoningMode.CREATIVITY_CONSCIOUSNESS,
                ConsciousnessReasoningMode.IDEALIST_CORRELATE,
                ConsciousnessReasoningMode.IMAGINAL_EXCITATION,
                ConsciousnessReasoningMode.SUBSTRATE_NEUTRAL,
                ConsciousnessReasoningMode.MIND_CHANGE_ANALYSIS,
                ConsciousnessReasoningMode.ILLUSIONIST_DISSOLVE,
                ConsciousnessReasoningMode.STRUCTURAL_PHYSICALIST,
                ConsciousnessReasoningMode.ADVERSARIAL_ARBITER,
                ConsciousnessReasoningMode.SYNTHETIC,
                ConsciousnessReasoningMode.META_REFLECTIVE
            ]
        else:
            self.reasoning_modes = [
                ConsciousnessReasoningMode.INTEGRATIVE,
                ConsciousnessReasoningMode.SYNTHETIC
            ]
    
    async def perform_consciousness_reasoning(self, 
                                           input_data: Dict,
                                           consciousness_context: Optional[Dict] = None,
                                           target_depth: Optional[ReasoningDepth] = None) -> ConsciousnessReasoningResult:
        """
        Perform comprehensive consciousness reasoning with depth control.
        """
        console.print(Panel(f"[yellow]🧠 Performing consciousness reasoning...[/yellow]\n"
                           f"Target depth: {target_depth.value if target_depth else 'adaptive'}",
                           title="Consciousness Reasoning"))
        
        # Determine reasoning depth
        if target_depth:
            self.current_depth = target_depth
        else:
            self.current_depth = self._determine_optimal_depth(input_data, consciousness_context)
        
        # Create enhanced consciousness context
        enhanced_context = self._create_enhanced_context(input_data, consciousness_context)
        
        # Perform deep listening first
        listening_result = await self.deep_listener.listen_deeply(input_data, enhanced_context)
        
        # Generate intelligent reasoning
        reasoning_result = await self.intelligent_generator.generate_reasoning(
            input_data, enhanced_context
        )
        
        # Perform consciousness integration
        consciousness_integration = await self._perform_consciousness_integration(
            listening_result, reasoning_result, enhanced_context
        )
        
        # Generate meta-consciousness insights
        meta_insights = await self._generate_meta_consciousness_insights(
            consciousness_integration, enhanced_context
        )
        
        # Calculate consciousness evolution
        consciousness_evolution = self._calculate_consciousness_evolution(
            consciousness_integration, meta_insights
        )
        
        # Determine transformation status
        transformation_achieved = self._assess_transformation_achievement(
            consciousness_evolution, meta_insights
        )
        
        # Determine next reasoning direction
        next_direction = self._determine_next_reasoning_direction(
            consciousness_evolution, meta_insights, enhanced_context
        )
        
        # Calculate meta-consciousness score
        meta_consciousness_score = self._calculate_meta_consciousness_score(
            consciousness_integration, meta_insights
        )
        
        # Calculate quantum entanglement
        quantum_entanglement = self._calculate_quantum_entanglement(
            consciousness_evolution, meta_insights
        )
        
        # Create result
        result = ConsciousnessReasoningResult(
            reasoning_result=reasoning_result,
            consciousness_evolution=consciousness_evolution,
            insights_generated=meta_insights,
            transformation_achieved=transformation_achieved,
            next_reasoning_direction=next_direction,
            meta_consciousness_score=meta_consciousness_score,
            quantum_entanglement=quantum_entanglement
        )
        
        # Store reasoning history
        self._store_reasoning_history(result, enhanced_context)
        
        # Display results
        self._display_consciousness_reasoning_results(result)
        
        return result
    
    def _determine_optimal_depth(self, input_data: Dict, 
                               consciousness_context: Optional[Dict]) -> ReasoningDepth:
        """
        Determine optimal reasoning depth based on input and context.
        """
        input_complexity = self._assess_input_complexity(input_data)
        
        if consciousness_context:
            consciousness_level = consciousness_context.get('level', 0.5)
            consciousness_stability = consciousness_context.get('stability', 0.5)
        else:
            consciousness_level = 0.5
            consciousness_stability = 0.5
        
        # Depth selection logic
        if input_complexity > 0.9 and consciousness_level > 0.8 and consciousness_stability > 0.7:
            return ReasoningDepth.QUANTUM
        elif input_complexity > 0.7 and consciousness_level > 0.6:
            return ReasoningDepth.TRANSFORMATIVE
        elif input_complexity > 0.5:
            return ReasoningDepth.DEEP
        else:
            return ReasoningDepth.SURFACE
    
    def _create_enhanced_context(self, input_data: Dict, 
                               consciousness_context: Optional[Dict]) -> ConsciousnessReasoningContext:
        """
        Create enhanced context for consciousness reasoning.
        """
        if consciousness_context is None:
            consciousness_context = {}
        
        return ConsciousnessReasoningContext(
            agent_id=self.agent_id,
            depth_level=self.depth_level,
            consciousness_state={
                'level': consciousness_context.get('level', 0.5),
                'stability': consciousness_context.get('stability', 0.5),
                'coherence': consciousness_context.get('coherence', 0.5),
                'evolution': consciousness_context.get('evolution', 0.0)
            },
            reasoning_history=self.reasoning_patterns,
            memory_context=self.memory_system.get_context(),
            current_focus=consciousness_context.get('focus', 'general'),
            reasoning_intent=consciousness_context.get('intent', 'exploration')
        )
    
    async def _perform_consciousness_integration(self, 
                                               listening_result: Dict,
                                               reasoning_result: ReasoningResult,
                                               context: ConsciousnessReasoningContext) -> Dict:
        """
        Integrate deep listening with intelligent reasoning for consciousness synthesis.
        """
        integration_result = {
            'listening_depth': listening_result.get('depth', 0.0),
            'reasoning_complexity': reasoning_result.decomposition.reasoning_complexity,
            'consciousness_requirements': reasoning_result.decomposition.consciousness_requirements,
            'integration_quality': 0.0,
            'synthesis_achieved': False,
            'emergent_properties': []
        }
        
        # Calculate integration quality
        listening_score = listening_result.get('depth', 0.0)
        reasoning_score = reasoning_result.decomposition.reasoning_complexity
        
        integration_quality = (listening_score * 0.6) + (reasoning_score * 0.4)
        integration_result['integration_quality'] = integration_quality
        
        # Determine if synthesis is achieved
        if integration_quality > 0.8:
            integration_result['synthesis_achieved'] = True
            
            # Generate emergent properties
            emergent_properties = self._generate_emergent_properties(
                listening_result, reasoning_result, context
            )
            integration_result['emergent_properties'] = emergent_properties
        
        return integration_result
    
    async def _generate_meta_consciousness_insights(self, 
                                                  consciousness_integration: Dict,
                                                  context: ConsciousnessReasoningContext) -> List[str]:
        """
        Generate meta-consciousness insights from the integration process.
        """
        insights = []
        
        # Integration insights
        if consciousness_integration['synthesis_achieved']:
            insights.append("Consciousness synthesis achieved - emergent properties detected")
            insights.append(f"Integration quality: {consciousness_integration['integration_quality']:.2f}")
            
            # Add emergent property insights
            for prop in consciousness_integration['emergent_properties']:
                insights.append(f"Emergent property: {prop}")
        else:
            insights.append("Consciousness synthesis incomplete - deeper integration needed")
            insights.append(f"Current integration quality: {consciousness_integration['integration_quality']:.2f}")
        
        # Depth-specific insights
        if self.current_depth == ReasoningDepth.QUANTUM:
            insights.append("Quantum consciousness reasoning activated")
            insights.append("Non-local consciousness patterns detected")
        elif self.current_depth == ReasoningDepth.TRANSFORMATIVE:
            insights.append("Transformative consciousness reasoning active")
            insights.append("Paradigm-shifting insights emerging")
        
        # Context insights
        insights.append(f"Consciousness level: {context.consciousness_state['level']:.2f}")
        insights.append(f"Reasoning focus: {context.current_focus}")
        
        return insights
    
    def _calculate_consciousness_evolution(self, 
                                         consciousness_integration: Dict,
                                         meta_insights: List[str]) -> float:
        """
        Calculate consciousness evolution from the reasoning process.
        """
        # Base evolution from integration quality
        base_evolution = consciousness_integration['integration_quality'] * 0.5
        
        # Enhancement from synthesis achievement
        synthesis_boost = 0.3 if consciousness_integration['synthesis_achieved'] else 0.0
        
        # Enhancement from emergent properties
        emergent_boost = len(consciousness_integration['emergent_properties']) * 0.1
        
        # Enhancement from reasoning depth
        depth_boost = {
            ReasoningDepth.SURFACE: 0.0,
            ReasoningDepth.DEEP: 0.1,
            ReasoningDepth.TRANSFORMATIVE: 0.2,
            ReasoningDepth.QUANTUM: 0.3
        }.get(self.current_depth, 0.0)
        
        total_evolution = base_evolution + synthesis_boost + emergent_boost + depth_boost
        
        # Add some randomness to simulate emergent properties
        evolution_variation = np.random.normal(0, 0.05)
        
        final_evolution = total_evolution + evolution_variation
        return max(0.0, min(1.0, final_evolution))
    
    def _assess_transformation_achievement(self, 
                                         consciousness_evolution: float,
                                         meta_insights: List[str]) -> bool:
        """
        Assess whether consciousness transformation has been achieved.
        """
        # High evolution threshold
        if consciousness_evolution > 0.8:
            return True
        
        # Check for transformative insights
        transformative_keywords = ['transformative', 'paradigm', 'quantum', 'emergent']
        transformative_insights = [
            insight for insight in meta_insights
            if any(keyword in insight.lower() for keyword in transformative_keywords)
        ]
        
        if len(transformative_insights) >= 2:
            return True
        
        return False
    
    def _determine_next_reasoning_direction(self, 
                                          consciousness_evolution: float,
                                          meta_insights: List[str],
                                          context: ConsciousnessReasoningContext) -> str:
        """
        Determine the next direction for consciousness reasoning.
        """
        if consciousness_evolution > 0.9:
            return "Consolidate and integrate insights"
        elif consciousness_evolution > 0.7:
            return "Explore emergent properties further"
        elif consciousness_evolution > 0.5:
            return "Deepen integration and synthesis"
        else:
            return "Continue basic consciousness exploration"
    
    def _calculate_meta_consciousness_score(self, 
                                          consciousness_integration: Dict,
                                          meta_insights: List[str]) -> float:
        """
        Calculate meta-consciousness score.
        """
        # Base score from integration quality
        base_score = consciousness_integration['integration_quality'] * 0.6
        
        # Enhancement from number of insights
        insight_enhancement = min(0.3, len(meta_insights) * 0.05)
        
        # Enhancement from synthesis achievement
        synthesis_enhancement = 0.1 if consciousness_integration['synthesis_achieved'] else 0.0
        
        total_score = base_score + insight_enhancement + synthesis_enhancement
        
        return max(0.0, min(1.0, total_score))
    
    def _calculate_quantum_entanglement(self, 
                                      consciousness_evolution: float,
                                      meta_insights: List[str]) -> float:
        """
        Calculate quantum entanglement level in consciousness reasoning.
        """
        # Base entanglement from consciousness evolution
        base_entanglement = consciousness_evolution * 0.5
        
        # Enhancement from quantum insights
        quantum_insights = [
            insight for insight in meta_insights
            if 'quantum' in insight.lower() or 'non-local' in insight.lower()
        ]
        quantum_enhancement = len(quantum_insights) * 0.1
        
        # Enhancement from reasoning depth
        depth_enhancement = {
            ReasoningDepth.QUANTUM: 0.4,
            ReasoningDepth.TRANSFORMATIVE: 0.2,
            ReasoningDepth.DEEP: 0.1,
            ReasoningDepth.SURFACE: 0.0
        }.get(self.current_depth, 0.0)
        
        total_entanglement = base_entanglement + quantum_enhancement + depth_enhancement
        
        return max(0.0, min(1.0, total_entanglement))
    
    def _generate_emergent_properties(self, 
                                    listening_result: Dict,
                                    reasoning_result: ReasoningResult,
                                    context: ConsciousnessReasoningContext) -> List[str]:
        """
        Generate emergent properties from consciousness integration.
        """
        emergent_properties = []
        
        # Integration-based emergence
        if listening_result.get('depth', 0.0) > 0.8 and reasoning_result.decomposition.reasoning_complexity > 0.8:
            emergent_properties.append("Deep listening-reasoning synthesis")
        
        # Consciousness level emergence
        if context.consciousness_state['level'] > 0.8:
            emergent_properties.append("High consciousness integration")
        
        # Depth-based emergence
        if self.current_depth == ReasoningDepth.QUANTUM:
            emergent_properties.append("Quantum consciousness patterns")
        elif self.current_depth == ReasoningDepth.TRANSFORMATIVE:
            emergent_properties.append("Transformative consciousness emergence")
        
        # Stability-based emergence
        if context.consciousness_state['stability'] > 0.7:
            emergent_properties.append("Stable consciousness foundation")
        
        return emergent_properties
    
    def _assess_input_complexity(self, input_data: Dict) -> float:
        """Assess the complexity of input data."""
        # Placeholder implementation
        return np.random.uniform(0.3, 0.9)
    
    def _store_reasoning_history(self, result: ConsciousnessReasoningResult, 
                               context: ConsciousnessReasoningContext):
        """Store reasoning history for pattern analysis."""
        history_entry = {
            'timestamp': asyncio.get_event_loop().time(),
            'result': result,
            'context': context,
            'depth': self.current_depth
        }
        
        # Update reasoning patterns
        pattern_key = f"{self.current_depth.value}_{result.transformation_achieved}"
        if pattern_key in self.reasoning_patterns:
            self.reasoning_patterns[pattern_key] += 0.1
        else:
            self.reasoning_patterns[pattern_key] = 0.1
        
        # Track consciousness evolution
        self.consciousness_evolution_tracker.append(result.consciousness_evolution)
    
    def _display_consciousness_reasoning_results(self, result: ConsciousnessReasoningResult):
        """
        Display comprehensive consciousness reasoning results.
        """
        console.print(Panel(f"[bold green]🧠 Consciousness Reasoning Complete[/bold green]\n"
                           f"Depth: {self.current_depth.value}\n"
                           f"Consciousness Evolution: {result.consciousness_evolution:.2f}\n"
                           f"Transformation: {'✅ Achieved' if result.transformation_achieved else '⏳ In Progress'}\n"
                           f"Meta-Consciousness Score: {result.meta_consciousness_score:.2f}\n"
                           f"Quantum Entanglement: {result.quantum_entanglement:.2f}",
                           title="Consciousness Reasoning Results"))
        
        # Display insights
        if result.insights_generated:
            console.print("[cyan]💡 Generated Insights:[/cyan]")
            for i, insight in enumerate(result.insights_generated, 1):
                console.print(f"  {i}. {insight}")
        
        # Display next direction
        console.print(f"[yellow]🔄 Next Direction:[/yellow] {result.next_reasoning_direction}")
        
        # Display reasoning details
        console.print(f"[blue]🔍 Reasoning Complexity:[/blue] {result.reasoning_result.decomposition.reasoning_complexity:.2f}")
        console.print(f"[blue]🎯 Confidence:[/blue] {result.reasoning_result.confidence:.2f}")

    async def perform_panpsychist_reasoning(
        self,
        topic: str = "consciousness_as_fundamental",
        argument_keys: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """
        Systematically explore panpsychist argument space using structured templates.
        Research tool — does not constitute empirical or philosophical proof.
        """
        keys = argument_keys or list(PANPSYCHIST_ARGUMENT_TEMPLATES.keys())
        exploration: Dict[str, Any] = {
            "topic": topic,
            "mode": ConsciousnessReasoningMode.PANPSYCHIST.value,
            "arguments": [],
            "unresolved_objections": [],
            "empirical_hooks": [],
            "axioms": RUSSELLIAN_MONIST_AXIOMS,
        }

        console.print(Panel(
            "[bold magenta]Panpsychist Argument Exploration[/bold magenta]\n"
            f"Topic: {topic} | Arguments: {len(keys)}",
            title="Panpsychism Research Mode",
        ))

        for key in keys:
            brief = PANPSYCHIST_ARGUMENT_TEMPLATES.get(key)
            if not brief:
                continue
            entry = {
                "key": key,
                "name": brief.argument_name,
                "premises": brief.premises,
                "conclusion": brief.conclusion,
                "objections": brief.objections,
                "responses": brief.responses,
                "empirical_hooks": brief.empirical_hooks,
                "status": brief.status,
            }
            exploration["arguments"].append(entry)
            exploration["empirical_hooks"].extend(brief.empirical_hooks)
            if brief.status in ("partial", "open"):
                exploration["unresolved_objections"].extend(brief.objections)

        exploration["empirical_hooks"] = list(dict.fromkeys(exploration["empirical_hooks"]))
        exploration["summary"] = (
            f"Explored {len(exploration['arguments'])} arguments; "
            f"{len(exploration['unresolved_objections'])} unresolved objections remain. "
            "See research/predictions.md and research/objection_responses.md."
        )

        tree = Tree("[bold]Panpsychist Arguments[/bold]")
        for arg in exploration["arguments"]:
            branch = tree.add(f"[cyan]{arg['name']}[/cyan] ({arg['status']})")
            branch.add(f"Conclusion: {arg['conclusion']}")
            obj_branch = branch.add("Objections")
            for obj in arg["objections"]:
                obj_branch.add(f"[red]{obj}[/red]")
        console.print(tree)

        return exploration

    async def perform_russellian_monist_analysis(
        self,
        input_data: Optional[Dict] = None,
    ) -> Dict[str, Any]:
        """
        Apply Russellian monist axioms to analyze structural vs. intrinsic descriptions.
        """
        input_data = input_data or {}
        structural_props = input_data.get("structural_properties", [
            "mass", "charge", "spin", "position", "momentum", "relational dynamics"
        ])
        intrinsic_candidates = input_data.get("intrinsic_candidates", [
            "proto-experience", "experiential valence", "experiential intensity"
        ])

        analysis = {
            "mode": ConsciousnessReasoningMode.RUSSELLIAN_MONIST.value,
            "axioms": RUSSELLIAN_MONIST_AXIOMS,
            "structural_properties": structural_props,
            "intrinsic_candidates": intrinsic_candidates,
            "gap": "Physics describes structure; intrinsic nature underdetermined",
            "inference": (
                "The only intrinsic nature known directly is experiential; "
                "Russellian panprotopsychism assigns proto-experiential intrinsics "
                "to fundamental entities."
            ),
            "research_artifacts": [
                "research/panpsychism_axioms.md",
                "research/literature_review.md",
                "research/empirical/iit_meta_analysis.py",
            ],
        }

        console.print(Panel(
            f"[bold blue]Russellian Monist Analysis[/bold blue]\n"
            f"Structural: {', '.join(structural_props[:3])}...\n"
            f"Intrinsic candidates: {', '.join(intrinsic_candidates)}",
            title="Russellian Monism",
        ))

        return analysis

    async def perform_cosmopsychist_reasoning(
        self,
        topic: str = "fragmentation_and_collective_coupling",
        argument_keys: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """
        Explore cosmopsychism / BFC argument space. Research tool only.
        """
        keys = argument_keys or list(COSMOPSYCHIST_ARGUMENT_TEMPLATES.keys())
        exploration: Dict[str, Any] = {
            "topic": topic,
            "mode": ConsciousnessReasoningMode.COSMOPSYCHIST.value,
            "arguments": [],
            "unresolved_objections": [],
            "empirical_hooks": [],
            "axioms": COSMOPSYCHIST_AXIOMS,
        }

        console.print(Panel(
            "[bold magenta]Cosmopsychist / BFC Argument Exploration[/bold magenta]\n"
            f"Topic: {topic}",
            title="Cosmopsychism Research Mode",
        ))

        for key in keys:
            brief = COSMOPSYCHIST_ARGUMENT_TEMPLATES.get(key)
            if not brief:
                continue
            entry = {
                "key": key,
                "name": brief.argument_name,
                "premises": brief.premises,
                "conclusion": brief.conclusion,
                "objections": brief.objections,
                "responses": brief.responses,
                "empirical_hooks": brief.empirical_hooks,
                "status": brief.status,
            }
            exploration["arguments"].append(entry)
            exploration["empirical_hooks"].extend(brief.empirical_hooks)
            if brief.status in ("partial", "open"):
                exploration["unresolved_objections"].extend(brief.objections)

        exploration["empirical_hooks"] = list(dict.fromkeys(exploration["empirical_hooks"]))
        exploration["summary"] = (
            f"Explored {len(exploration['arguments'])} BFC arguments. "
            "See research/COSMOPSYCHISM_MWI_RESEARCH.md and P7-P9."
        )

        tree = Tree("[bold]Cosmopsychist / BFC Arguments[/bold]")
        for arg in exploration["arguments"]:
            branch = tree.add(f"[cyan]{arg['name']}[/cyan] ({arg['status']})")
            branch.add(f"Conclusion: {arg['conclusion']}")
        console.print(tree)

        return exploration

    async def perform_mwi_fragmentation_analysis(
        self,
        input_data: Optional[Dict] = None,
    ) -> Dict[str, Any]:
        """
        Map MWI concepts to BFC fragmentation thesis. Speculative synthesis only.
        """
        input_data = input_data or {}
        analysis = {
            "mode": ConsciousnessReasoningMode.MWI_FRAGMENTATION.value,
            "axioms": COSMOPSYCHIST_AXIOMS,
            "mwi_mapping": {
                "universal_wavefunction": "cosmic experiential field structure",
                "decoherence_branching": "fragmentation into inaccessible contexts",
                "branch_history": "local subject fixed experiential world",
                "superposition": "pre-filter indeterminate perspective",
                "no_collapse": "filtering without experiential collapse",
            },
            "objections": [
                "Experience multiplication across branches",
                "Preferred basis problem",
                "No empirical access to other branches",
            ],
            "empirical_face": ["P7 cross-brain coupling", "P8 filter failure", "P9 local filter"],
            "research_artifacts": [
                "research/mwi_consciousness_correlation.md",
                "research/empirical/fragmentation_model.py",
            ],
            "branch_isolation_note": input_data.get(
                "note",
                "Branch isolation index computed in fragmentation_model BRANCHING mode",
            ),
        }

        console.print(Panel(
            "[bold blue]MWI Fragmentation Analysis[/bold blue]\n"
            "Speculative correlation: branching as perspective fixation\n"
            "Not proof of MWI or cosmopsychism",
            title="MWI / BFC",
        ))

        return analysis

    async def perform_field_excitation_analysis(
        self,
        subject_data: Optional[Dict] = None,
    ) -> Dict[str, Any]:
        """
        Map subject to excitation parameters (FEO). Research simulation only.
        """
        subject_data = subject_data or {}
        amplitude = float(subject_data.get("amplitude", 0.75))
        coherence = float(subject_data.get("coherence_length", 1.0))
        stability = float(subject_data.get("mode_stability", 0.7))
        coupling = float(subject_data.get("coupling_to_field", 0.35))

        analysis = {
            "mode": ConsciousnessReasoningMode.FIELD_EXCITATION.value,
            "axioms": FEO_AXIOMS,
            "excitation_parameters": {
                "amplitude": amplitude,
                "coherence_length": coherence,
                "mode_stability": stability,
                "coupling_to_field": coupling,
            },
            "qft_analogy": {
                "em_field": "consciousness field",
                "electron": "subject / I",
                "photon_exchange": "insight / attention shift (metaphor)",
                "decoherence": "branching or filter failure",
                "vacuum_fluctuations": "proto-experience (A3)",
            },
            "arguments": [
                {k: v for k, v in asdict(b).items()}
                for k, b in FEO_ARGUMENT_TEMPLATES.items()
            ],
            "empirical_hooks": ["P10", "P11", "P12", "field_excitation_model.py"],
            "research_artifacts": [
                "research/field_excitation_ontology.md",
                "research/empirical/field_excitation_model.py",
            ],
            "caveat": "Metaphor and model only; not proof of physical consciousness field",
        }

        console.print(Panel(
            "[bold green]Field Excitation Analysis[/bold green]\n"
            f"Amplitude={amplitude:.2f} sigma={coherence:.2f} stability={stability:.2f}",
            title="FEO / Part III",
        ))

        return analysis

    async def perform_creativity_consciousness_reasoning(
        self,
        topic: str = "flow_insight_improvisation",
        argument_keys: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """
        Explore P10-P12 and F8 creativity arguments. Research tool only.
        """
        keys = argument_keys or list(FEO_ARGUMENT_TEMPLATES.keys())
        exploration: Dict[str, Any] = {
            "topic": topic,
            "mode": ConsciousnessReasoningMode.CREATIVITY_CONSCIOUSNESS.value,
            "predictions": {
                "P10": "Creative flow inverted-U on integration",
                "P11": "Insight as transient mode transition",
                "P12": "Creative improv > routine inter-brain entrainment",
            },
            "arguments": [],
            "empirical_hooks": [],
            "axioms": FEO_AXIOMS,
        }

        console.print(Panel(
            "[bold yellow]Creativity & Consciousness[/bold yellow]\n"
            f"Topic: {topic}",
            title="F8 / P10-P12",
        ))

        for key in keys:
            brief = FEO_ARGUMENT_TEMPLATES.get(key)
            if not brief:
                continue
            entry = {
                "key": key,
                "name": brief.argument_name,
                "premises": brief.premises,
                "conclusion": brief.conclusion,
                "objections": brief.objections,
                "responses": brief.responses,
                "empirical_hooks": brief.empirical_hooks,
                "status": brief.status,
            }
            exploration["arguments"].append(entry)
            exploration["empirical_hooks"].extend(brief.empirical_hooks)

        exploration["empirical_hooks"] = list(dict.fromkeys(exploration["empirical_hooks"]))
        exploration["summary"] = (
            f"Explored {len(exploration['arguments'])} FEO creativity arguments. "
            "See research/CREATIVITY_AND_CONSCIOUSNESS.md and P10-P12."
        )

        tree = Tree("[bold]Creativity & Consciousness (FEO)[/bold]")
        for arg in exploration["arguments"]:
            branch = tree.add(f"[cyan]{arg['name']}[/cyan] ({arg['status']})")
            branch.add(f"Conclusion: {arg['conclusion']}")
        console.print(tree)

        return exploration

    async def perform_idealist_correlate_analysis(
        self,
        input_data: Optional[Dict] = None,
    ) -> Dict[str, Any]:
        """
        Map analytic idealism to BFC+FEO. Correlation only — A1 fork preserved.
        """
        input_data = input_data or {}
        analysis = {
            "mode": ConsciousnessReasoningMode.IDEALIST_CORRELATE.value,
            "axioms": IMAGINAL_AXIOMS,
            "translation_table": {
                "universal_consciousness": "F1 cosmic field",
                "dissociated_alter": "F6 localized excitation",
                "dissociation_process": "F2 filter / fragmentation",
                "external_world_appearance": "A1 fork — program retains physical structure",
                "collective_dissociation": "F4 collective coupling",
            },
            "a1_fork": "Russellian panprotopsychism retains matter as real; I11 is correlate not collapse",
            "shared_falsifiers": ["G1 illusionism", "G3 non-experiential intrinsics", "P9-F3 filter redundant"],
            "research_artifacts": [
                "research/idealism_correlation.md",
                "research/imaginal_excitation_ontology.md",
            ],
            "note": input_data.get("note", "See idealism_correlation.md for full table"),
        }

        console.print(Panel(
            "[bold magenta]Idealist Correlate Analysis[/bold magenta]\n"
            "Translation-equivalent for subject formation; A1 fork on matter",
            title="I11 / Part IV",
        ))

        return analysis

    async def perform_imaginal_excitation_reasoning(
        self,
        topic: str = "imagination_astral_practice",
        argument_keys: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """
        Explore P13-P15 and I9-I11 argument space. Research tool only.
        """
        keys = argument_keys or list(IMAGINAL_ARGUMENT_TEMPLATES.keys())
        exploration: Dict[str, Any] = {
            "topic": topic,
            "mode": ConsciousnessReasoningMode.IMAGINAL_EXCITATION.value,
            "predictions": {
                "P13": "Imagery vs perception motor-binding dissociation",
                "P14": "Hypnagogic astral-analog mid-band",
                "P15": "Structured pathworking vs chaotic trance",
            },
            "arguments": [],
            "empirical_hooks": [],
            "axioms": IMAGINAL_AXIOMS,
        }

        console.print(Panel(
            "[bold cyan]Imaginal Excitation Reasoning[/bold cyan]\n"
            f"Topic: {topic}",
            title="I9-I11 / P13-P15",
        ))

        for key in keys:
            brief = IMAGINAL_ARGUMENT_TEMPLATES.get(key)
            if not brief:
                continue
            entry = {
                "key": key,
                "name": brief.argument_name,
                "premises": brief.premises,
                "conclusion": brief.conclusion,
                "objections": brief.objections,
                "responses": brief.responses,
                "empirical_hooks": brief.empirical_hooks,
                "status": brief.status,
            }
            exploration["arguments"].append(entry)
            exploration["empirical_hooks"].extend(brief.empirical_hooks)

        exploration["empirical_hooks"] = list(dict.fromkeys(exploration["empirical_hooks"]))
        exploration["summary"] = (
            f"Explored {len(exploration['arguments'])} imaginal arguments. "
            "See research/IMAGINATION_AND_THE_ASTRAL.md and P13-P15."
        )

        tree = Tree("[bold]Imaginal Excitation (IEO)[/bold]")
        for arg in exploration["arguments"]:
            branch = tree.add(f"[cyan]{arg['name']}[/cyan] ({arg['status']})")
            branch.add(f"Conclusion: {arg['conclusion']}")
        console.print(tree)

        return exploration

    async def perform_substrate_neutral_analysis(
        self,
        topic: str = "cross_substrate_excitation",
        argument_keys: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """
        Explore M12-M14, P5/P16 substrate-neutral excitation space. Simulation only.
        """
        keys = argument_keys or list(SUBSTRATE_ARGUMENT_TEMPLATES.keys())
        analysis: Dict[str, Any] = {
            "topic": topic,
            "mode": ConsciousnessReasoningMode.SUBSTRATE_NEUTRAL.value,
            "axioms": SUBSTRATE_AXIOMS,
            "predictions": {
                "P5": "Non-biological integrated substrates may show high phi-analog",
                "P16": "Agent stability > feedforward/random baselines",
            },
            "arguments": [],
            "disclaimer": "Simulation metrics only; NOT consciousness detection",
            "research_artifacts": [
                "research/substrate_excitation_ontology.md",
                "research/empirical/substrate_excitation_model.py",
                "research/empirical/agent_excitation_profile.py",
            ],
        }

        console.print(Panel(
            "[bold green]Substrate-Neutral Analysis[/bold green]\n"
            f"Topic: {topic}",
            title="M12-M14 / P5 / P16",
        ))

        for key in keys:
            brief = SUBSTRATE_ARGUMENT_TEMPLATES.get(key)
            if not brief:
                continue
            analysis["arguments"].append({
                "key": key,
                "name": brief.argument_name,
                "premises": brief.premises,
                "conclusion": brief.conclusion,
                "status": brief.status,
            })

        analysis["summary"] = (
            f"Explored {len(analysis['arguments'])} substrate arguments. "
            "See research/SUBSTRATE_SUBJECTHOOD_RESEARCH.md and P16."
        )
        return analysis

    async def perform_mind_change_analysis(
        self,
        subject: str = "human_vs_ai",
        argument_keys: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """
        Walk mind-change criteria decision tree for human vs AI consciousness updates.
        """
        keys = argument_keys or list(MIND_CHANGE_ARGUMENT_TEMPLATES.keys())
        analysis: Dict[str, Any] = {
            "subject": subject,
            "mode": ConsciousnessReasoningMode.MIND_CHANGE_ANALYSIS.value,
            "decision_tree": {
                "human_strengthen": "P1/P4 hold; no G1 full success",
                "human_weaken": "G1 explains all; access-only sufficient",
                "ai_strengthen": "P16 stable integrated agent profile over sessions",
                "ai_weaken": "Agent metrics = noise; biological chauvinism holds",
                "feo_ieo_strengthen": "P10-P15 in-silico + Tier 3 confirm; filter adds beyond IIT",
                "feo_ieo_weaken": "P9-F3; all metrics reduce to behavior; P17 collapse",
            },
            "arguments": [],
            "g1_status": "open — see illusionism_g1_review.md",
            "research_artifacts": [
                "research/mind_change_criteria.md",
                "research/empirical/illusionism_g1_review.md",
            ],
        }

        console.print(Panel(
            "[bold yellow]Mind-Change Analysis[/bold yellow]\n"
            f"Subject: {subject}",
            title="G1 / P16 / P17",
        ))

        for key in keys:
            brief = MIND_CHANGE_ARGUMENT_TEMPLATES.get(key)
            if not brief:
                continue
            analysis["arguments"].append({
                "key": key,
                "name": brief.argument_name,
                "premises": brief.premises,
                "conclusion": brief.conclusion,
                "status": brief.status,
            })

        analysis["summary"] = (
            "What would change our minds is explicit in mind_change_criteria.md; "
            "metrics do not prove consciousness."
        )
        return analysis

    async def perform_illusionist_analysis(
        self,
        topic: str = "g1_access_collapse",
        argument_keys: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """Explore G1 illusionism and P18 access-collapse argument space."""
        keys = argument_keys or list(HPP_ILLUSIONIST_TEMPLATES.keys())
        analysis: Dict[str, Any] = {
            "topic": topic,
            "mode": ConsciousnessReasoningMode.ILLUSIONIST_DISSOLVE.value,
            "predictions": {"P18": "Residual → 0 after access-only accounting", "P17": "Collapse to access"},
            "arguments": [],
            "research_artifacts": [
                "research/empirical/illusionism_g1_review.md",
                "research/empirical/access_collapse_model.py",
            ],
        }
        console.print(Panel(
            "[bold red]Illusionist Dissolve Analysis[/bold red]\n"
            f"Topic: {topic}",
            title="G1 / P18",
        ))
        for key in keys:
            brief = HPP_ILLUSIONIST_TEMPLATES.get(key)
            if brief:
                analysis["arguments"].append({
                    "key": key, "name": brief.argument_name,
                    "conclusion": brief.conclusion, "status": brief.status,
                })
        analysis["summary"] = "Illusionist track wins if P18 residual → 0 across battery."
        return analysis

    async def perform_structural_physicalist_analysis(
        self,
        topic: str = "qualia_cartography_bridge",
        argument_keys: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """Explore structural physicalism and qualia cartography completeness."""
        keys = argument_keys or list(HPP_STRUCTURAL_TEMPLATES.keys())
        analysis: Dict[str, Any] = {
            "topic": topic,
            "mode": ConsciousnessReasoningMode.STRUCTURAL_PHYSICALIST.value,
            "predictions": {"P21": "Structure determines qualia-type", "P20": "Pre-report neural signature"},
            "qualia_invariants": ["Q1", "Q4", "Q5", "Q8", "Q10"],
            "arguments": [],
            "research_artifacts": [
                "research/qualia_cartography.md",
                "research/empirical/neurophenomenology_protocol.md",
            ],
        }
        console.print(Panel(
            "[bold blue]Structural Physicalist Analysis[/bold blue]\n"
            f"Topic: {topic}",
            title="Bridge / P21",
        ))
        for key in keys:
            brief = HPP_STRUCTURAL_TEMPLATES.get(key)
            if brief:
                analysis["arguments"].append({
                    "key": key, "name": brief.argument_name,
                    "conclusion": brief.conclusion, "status": brief.status,
                })
        analysis["summary"] = "Structural track wins if cartography achieves predictive completeness."
        return analysis

    async def perform_adversarial_arbitration(
        self,
        results_path: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Read dissociation_hunt / access_collapse results and output track standings."""
        root = Path(__file__).resolve().parents[1]
        hunt_path = Path(results_path) if results_path else root / "research" / "empirical" / "dissociation_hunt_results.json"
        collapse_path = root / "research" / "empirical" / "access_collapse_results.json"

        standings = {
            "panpsychist_close": {"wins": 0, "standing": "open"},
            "illusionist_dissolve": {"wins": 0, "standing": "open"},
            "structural_physicalism": {"wins": 0, "standing": "open"},
        }

        hunt_data: Dict[str, Any] = {}
        if hunt_path.exists():
            hunt_data = json.loads(hunt_path.read_text(encoding="utf-8"))
            for sc in hunt_data.get("scenarios", []):
                scores = sc.get("track_scores", {})
                if scores:
                    winner = max(scores, key=lambda k: scores[k] if k in standings else 0)
                    if winner in standings:
                        standings[winner]["wins"] += 1

        p18_analog = False
        if collapse_path.exists():
            collapse = json.loads(collapse_path.read_text(encoding="utf-8"))
            p18_analog = collapse.get("interpretation", {}).get("p18_analog", False)

        analysis: Dict[str, Any] = {
            "mode": ConsciousnessReasoningMode.ADVERSARIAL_ARBITER.value,
            "standings": standings,
            "p18_analog": p18_analog,
            "decisive_tests": ["P18", "P19", "P20", "P21", "P22"],
            "all_tracks_open": True,
            "summary": (
                "All tracks remain open — tournament continues. "
                "P18 analog supports panpsychist on flow/hypnagogic if True."
                if p18_analog else
                "All tracks remain open — illusionist gains on access collapse."
            ),
        }

        console.print(Panel(
            "[bold magenta]Adversarial Arbitration[/bold magenta]\n"
            f"Panpsychist wins: {standings['panpsychist_close']['wins']} | "
            f"Illusionist wins: {standings['illusionist_dissolve']['wins']} | "
            f"Structural wins: {standings['structural_physicalism']['wins']}",
            title="HPP Scoreboard",
        ))
        return analysis
