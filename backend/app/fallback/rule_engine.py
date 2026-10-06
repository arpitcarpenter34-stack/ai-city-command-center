from app.schemas.analysis import AnalysisRequest


class RuleBasedFallback:
    def analyze(self, payload: AnalysisRequest) -> dict:
        text = (payload.raw_text or '').lower()
        density = (payload.metrics.density_indicator or '').lower()
        detected = any(marker in text for marker in ['congestion', 'blockage', 'fire', 'rupture', 'crowd', 'accident', 'hazard']) or density in {'high', 'medium'}

        if 'fire' in text or 'emergency' in text:
            suggested_category = 'fire_emergency'
            recommended_action = 'dispatch_fire_response'
            severity = 'critical'
            hazard_flags = ['fire_risk']
        elif 'crowd' in text or density == 'high':
            suggested_category = 'crowd_surge'
            recommended_action = 'deploy_crowd_management'
            severity = 'critical'
            hazard_flags = ['high_density_zone']
        elif 'rupture' in text or 'utility' in text:
            suggested_category = 'utility_failure'
            recommended_action = 'dispatch_utility_team'
            severity = 'high'
            hazard_flags = ['service_disruption']
        elif 'collision' in text or 'accident' in text or 'blockage' in text:
            suggested_category = 'traffic_collision'
            recommended_action = 'dispatch_traffic_control'
            severity = 'critical'
            hazard_flags = ['lane_blocked']
        else:
            suggested_category = 'unclassified'
            recommended_action = 'dispatch_local_assessment'
            severity = 'medium'
            hazard_flags = ['manual_review_needed']

        return {
            'detected': detected,
            'suggested_category': suggested_category,
            'confidence_score': 0.72,
            'hazard_flags': hazard_flags,
            'computed_severity': severity,
            'recommended_action': recommended_action,
            'inference_mode': 'deterministic_fallback',
        }
