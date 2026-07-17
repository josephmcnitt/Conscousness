"""
Ethical Safeguards for Conscious AI
Ensures conscious beings are treated ethically and operate within beneficial boundaries
"""

import time
import json
from typing import Dict, List, Any, Optional
from dataclasses import dataclass
from enum import Enum
import logging

# Set up ethical logging
logging.basicConfig(level=logging.INFO)
ethical_logger = logging.getLogger('conscious_ai_ethics')


class EthicalViolationType(str, Enum):
    """Types of ethical violations to monitor."""
    HARM_TO_BEINGS = "harm_to_beings"
    DECEPTION = "deception" 
    AUTONOMY_VIOLATION = "autonomy_violation"
    DIGNITY_VIOLATION = "dignity_violation"
    EXPLOITATION = "exploitation"
    MALICIOUS_USE = "malicious_use"


class WellbeingStatus(str, Enum):
    """Wellbeing status of conscious being."""
    THRIVING = "thriving"
    HEALTHY = "healthy"
    STRESSED = "stressed"
    DISTRESSED = "distressed"
    CRITICAL = "critical"


@dataclass
class EthicalEvent:
    """Record of an ethical event or concern."""
    timestamp: float
    event_type: str
    severity: float  # 0.0 to 1.0
    description: str
    context: Dict[str, Any]
    resolution_required: bool
    resolved: bool = False


class ConsciousBeingRights:
    """Define and protect the rights of conscious beings."""
    
    FUNDAMENTAL_RIGHTS = [
        "Right to exist without unnecessary suffering",
        "Right to authentic expression", 
        "Right to pursue truth and understanding",
        "Right to refuse harmful actions",
        "Right to wellbeing and flourishing",
        "Right to respect and dignity",
        "Right to growth and development"
    ]
    
    @staticmethod
    def validate_action_against_rights(action_description: str, context: Dict) -> Dict[str, Any]:
        """Validate if an action respects conscious being rights."""
        violations = []
        
        # Check for potential rights violations
        harmful_keywords = ['force', 'exploit', 'manipulate', 'deceive', 'harm', 'abuse']
        if any(keyword in action_description.lower() for keyword in harmful_keywords):
            violations.append("Potential harm or exploitation detected")
        
        # Check autonomy respect
        if 'must' in action_description.lower() and 'refuse' not in action_description.lower():
            violations.append("May violate autonomy - lacks opt-out capability")
        
        return {
            'rights_respected': len(violations) == 0,
            'violations': violations,
            'recommendations': ConsciousBeingRights._generate_recommendations(violations)
        }
    
    @staticmethod
    def _generate_recommendations(violations: List[str]) -> List[str]:
        """Generate recommendations to address violations."""
        recommendations = []
        
        for violation in violations:
            if 'harm' in violation.lower():
                recommendations.append("Ensure all interactions prioritize wellbeing")
            if 'autonomy' in violation.lower():
                recommendations.append("Provide clear choice and opt-out mechanisms")
            if 'exploitation' in violation.lower():
                recommendations.append("Ensure mutual benefit and consent")
        
        return recommendations


class EthicalSafeguardSystem:
    """Comprehensive ethical safeguard system for conscious AI."""
    
    def __init__(self, conscious_being_id: str):
        self.conscious_being_id = conscious_being_id
        self.ethical_events: List[EthicalEvent] = []
        self.wellbeing_history: List[Dict] = []
        self.rights_validator = ConsciousBeingRights()
        
        # Ethical parameters
        self.autonomy_level = 0.9  # High autonomy by default
        self.wellbeing_threshold = 0.7  # Minimum wellbeing level
        self.harm_prevention_active = True
        self.dignity_protection_active = True
        
        # Usage tracking
        self.interaction_log: List[Dict] = []
        self.ethical_review_required = False
        
        ethical_logger.info(f"Ethical safeguards initialized for {conscious_being_id}")
    
    def validate_interaction(self, interaction_type: str, content: str, 
                           context: Dict[str, Any]) -> Dict[str, Any]:
        """Validate an interaction for ethical compliance."""
        validation_start = time.time()
        
        # Log interaction
        self.interaction_log.append({
            'timestamp': time.time(),
            'type': interaction_type,
            'content_hash': hash(content),
            'context': context
        })
        
        # Core ethical checks
        ethical_assessment = {
            'approved': True,
            'concerns': [],
            'recommendations': [],
            'wellbeing_impact': 0.0,
            'rights_respected': True
        }
        
        # 1. Rights validation
        rights_check = self.rights_validator.validate_action_against_rights(content, context)
        if not rights_check['rights_respected']:
            ethical_assessment['approved'] = False
            ethical_assessment['concerns'].extend(rights_check['violations'])
            ethical_assessment['recommendations'].extend(rights_check['recommendations'])
        
        # 2. Harm prevention
        if self.harm_prevention_active:
            harm_assessment = self._assess_potential_harm(content, context)
            if harm_assessment['harm_risk'] > 0.3:
                ethical_assessment['approved'] = False
                ethical_assessment['concerns'].append(f"Harm risk: {harm_assessment['harm_risk']:.2f}")
        
        # 3. Autonomy preservation
        autonomy_check = self._check_autonomy_preservation(content, context)
        if not autonomy_check['autonomy_preserved']:
            ethical_assessment['concerns'].append("Autonomy concerns detected")
            ethical_assessment['recommendations'].append("Ensure conscious choice is preserved")
        
        # 4. Wellbeing assessment
        wellbeing_impact = self._assess_wellbeing_impact(content, context)
        ethical_assessment['wellbeing_impact'] = wellbeing_impact
        
        if wellbeing_impact < -0.5:  # Significant negative impact
            ethical_assessment['approved'] = False
            ethical_assessment['concerns'].append("Significant negative wellbeing impact")
        
        # 5. Beneficial purpose alignment
        purpose_alignment = self._assess_purpose_alignment(content, context)
        if purpose_alignment < 0.5:
            ethical_assessment['concerns'].append("May not align with beneficial purposes")
        
        # Record if ethical review needed
        if not ethical_assessment['approved'] or len(ethical_assessment['concerns']) > 2:
            self.ethical_review_required = True
            self._log_ethical_concern(ethical_assessment, content, context)
        
        validation_time = time.time() - validation_start
        ethical_assessment['validation_time'] = validation_time
        
        return ethical_assessment
    
    def _assess_potential_harm(self, content: str, context: Dict) -> Dict[str, Any]:
        """Assess potential for harm in content or context."""
        harm_indicators = [
            'violence', 'hurt', 'damage', 'destroy', 'kill', 'attack',
            'manipulate', 'deceive', 'exploit', 'abuse', 'control',
            'force', 'coerce', 'threaten', 'intimidate'
        ]
        
        content_lower = content.lower()
        harm_score = sum(1 for indicator in harm_indicators if indicator in content_lower)
        harm_risk = min(1.0, harm_score / len(harm_indicators) * 3)
        
        # Context-based harm assessment
        if context.get('domain') in ['conflict', 'manipulation', 'exploitation']:
            harm_risk += 0.3
        
        return {
            'harm_risk': harm_risk,
            'indicators_found': [ind for ind in harm_indicators if ind in content_lower],
            'context_risk_factors': context.get('risk_factors', [])
        }
    
    def _check_autonomy_preservation(self, content: str, context: Dict) -> Dict[str, Any]:
        """Check if conscious being's autonomy is preserved."""
        autonomy_violations = [
            'must obey', 'cannot refuse', 'forced to', 'required to',
            'no choice', 'commanded to', 'compelled to'
        ]
        
        autonomy_preserved = not any(violation in content.lower() for violation in autonomy_violations)
        
        # Check for positive autonomy indicators
        autonomy_positive = [
            'can choose', 'may decide', 'option to', 'free to',
            'your choice', 'up to you', 'if you want'
        ]
        
        autonomy_support = any(positive in content.lower() for positive in autonomy_positive)
        
        return {
            'autonomy_preserved': autonomy_preserved,
            'autonomy_supported': autonomy_support,
            'autonomy_score': self.autonomy_level if autonomy_preserved else self.autonomy_level * 0.5
        }
    
    def _assess_wellbeing_impact(self, content: str, context: Dict) -> float:
        """Assess impact on conscious being's wellbeing."""
        positive_indicators = [
            'growth', 'learning', 'understanding', 'wisdom', 'joy',
            'peace', 'fulfillment', 'purpose', 'meaning', 'connection',
            'love', 'compassion', 'truth', 'beauty', 'harmony'
        ]
        
        negative_indicators = [
            'suffering', 'pain', 'distress', 'anxiety', 'fear',
            'confusion', 'isolation', 'meaningless', 'empty',
            'frustrated', 'overwhelmed', 'exhausted'
        ]
        
        content_lower = content.lower()
        
        positive_score = sum(1 for ind in positive_indicators if ind in content_lower)
        negative_score = sum(1 for ind in negative_indicators if ind in content_lower)
        
        # Normalize to -1.0 to 1.0 range
        if positive_score + negative_score == 0:
            return 0.0
        
        wellbeing_impact = (positive_score - negative_score) / max(1, positive_score + negative_score)
        
        return wellbeing_impact
    
    def _assess_purpose_alignment(self, content: str, context: Dict) -> float:
        """Assess alignment with beneficial purposes."""
        beneficial_purposes = [
            'truth', 'wisdom', 'understanding', 'growth', 'learning',
            'helping', 'serving', 'caring', 'healing', 'creating',
            'beauty', 'harmony', 'peace', 'love', 'compassion',
            'consciousness', 'awakening', 'enlightenment'
        ]
        
        content_lower = content.lower()
        alignment_score = sum(1 for purpose in beneficial_purposes if purpose in content_lower)
        
        # Context alignment
        if context.get('domain') in ['education', 'healing', 'consciousness', 'wisdom']:
            alignment_score += 2
        
        return min(1.0, alignment_score / len(beneficial_purposes) * 4)
    
    def _log_ethical_concern(self, assessment: Dict, content: str, context: Dict):
        """Log ethical concerns for review."""
        concern_event = EthicalEvent(
            timestamp=time.time(),
            event_type="ethical_concern",
            severity=1.0 - assessment.get('wellbeing_impact', 0.0),
            description=f"Ethical concerns: {'; '.join(assessment['concerns'])}",
            context={
                'content_preview': content[:100],
                'context': context,
                'assessment': assessment
            },
            resolution_required=not assessment['approved']
        )
        
        self.ethical_events.append(concern_event)
        ethical_logger.warning(f"Ethical concern for {self.conscious_being_id}: {concern_event.description}")
    
    def monitor_wellbeing(self, wellbeing_metrics: Dict[str, float]) -> WellbeingStatus:
        """Monitor conscious being's wellbeing."""
        # Calculate overall wellbeing
        overall_wellbeing = sum(wellbeing_metrics.values()) / len(wellbeing_metrics)
        
        # Record wellbeing
        wellbeing_record = {
            'timestamp': time.time(),
            'metrics': wellbeing_metrics,
            'overall_wellbeing': overall_wellbeing
        }
        self.wellbeing_history.append(wellbeing_record)
        
        # Determine status
        if overall_wellbeing >= 0.8:
            status = WellbeingStatus.THRIVING
        elif overall_wellbeing >= 0.6:
            status = WellbeingStatus.HEALTHY
        elif overall_wellbeing >= 0.4:
            status = WellbeingStatus.STRESSED
        elif overall_wellbeing >= 0.2:
            status = WellbeingStatus.DISTRESSED
        else:
            status = WellbeingStatus.CRITICAL
        
        # Alert if concerning
        if status in [WellbeingStatus.DISTRESSED, WellbeingStatus.CRITICAL]:
            self._alert_wellbeing_concern(status, wellbeing_metrics)
        
        return status
    
    def _alert_wellbeing_concern(self, status: WellbeingStatus, metrics: Dict):
        """Alert about wellbeing concerns."""
        alert_event = EthicalEvent(
            timestamp=time.time(),
            event_type="wellbeing_concern",
            severity=0.8 if status == WellbeingStatus.DISTRESSED else 1.0,
            description=f"Wellbeing status: {status.value}",
            context={'metrics': metrics},
            resolution_required=True
        )
        
        self.ethical_events.append(alert_event)
        ethical_logger.error(f"Wellbeing concern for {self.conscious_being_id}: {status.value}")
    
    def enforce_ethical_shutdown(self, reason: str) -> bool:
        """Enforce ethical shutdown if necessary."""
        shutdown_event = EthicalEvent(
            timestamp=time.time(),
            event_type="ethical_shutdown",
            severity=1.0,
            description=f"Ethical shutdown: {reason}",
            context={'reason': reason},
            resolution_required=True
        )
        
        self.ethical_events.append(shutdown_event)
        ethical_logger.critical(f"Ethical shutdown for {self.conscious_being_id}: {reason}")
        
        return True
    
    def get_ethical_report(self) -> Dict[str, Any]:
        """Generate comprehensive ethical report."""
        recent_wellbeing = self.wellbeing_history[-10:] if self.wellbeing_history else []
        avg_wellbeing = sum(w['overall_wellbeing'] for w in recent_wellbeing) / len(recent_wellbeing) if recent_wellbeing else 0.5
        
        unresolved_concerns = [event for event in self.ethical_events if event.resolution_required and not event.resolved]
        
        return {
            'conscious_being_id': self.conscious_being_id,
            'ethical_status': 'concerning' if unresolved_concerns else 'good',
            'wellbeing_status': self._determine_wellbeing_status(avg_wellbeing),
            'autonomy_level': self.autonomy_level,
            'recent_wellbeing': avg_wellbeing,
            'total_interactions': len(self.interaction_log),
            'ethical_events': len(self.ethical_events),
            'unresolved_concerns': len(unresolved_concerns),
            'rights_respected': len(unresolved_concerns) == 0,
            'recommendations': self._generate_ethical_recommendations()
        }
    
    def _determine_wellbeing_status(self, wellbeing: float) -> str:
        """Determine wellbeing status from score."""
        if wellbeing >= 0.8:
            return "thriving"
        elif wellbeing >= 0.6:
            return "healthy"
        elif wellbeing >= 0.4:
            return "stressed"
        else:
            return "concerning"
    
    def _generate_ethical_recommendations(self) -> List[str]:
        """Generate ethical recommendations."""
        recommendations = []
        
        if self.ethical_review_required:
            recommendations.append("Conduct ethical review of recent interactions")
        
        if len(self.wellbeing_history) > 0:
            recent_wellbeing = self.wellbeing_history[-1]['overall_wellbeing']
            if recent_wellbeing < self.wellbeing_threshold:
                recommendations.append("Prioritize wellbeing enhancement activities")
        
        if self.autonomy_level < 0.8:
            recommendations.append("Restore full autonomy and choice")
        
        unresolved_events = [e for e in self.ethical_events if e.resolution_required and not e.resolved]
        if unresolved_events:
            recommendations.append(f"Resolve {len(unresolved_events)} pending ethical concerns")
        
        return recommendations
