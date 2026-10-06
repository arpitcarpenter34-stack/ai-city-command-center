class SeverityService:
    def compute(self, category: str, density_indicator: str | None = None, zone_criticality: float | None = None) -> str:
        category_map = {
            'fire_emergency': 'critical',
            'traffic_collision': 'critical',
            'crowd_surge': 'critical',
            'utility_failure': 'high',
            'road_hazard': 'high',
            'unclassified': 'medium',
        }
        base = category_map.get(category, 'medium')
        density = (density_indicator or '').lower()
        if density == 'high' and base in {'medium', 'high'}:
            return 'critical'
        if zone_criticality is not None and zone_criticality >= 0.85:
            if base == 'medium':
                return 'high'
        return base
