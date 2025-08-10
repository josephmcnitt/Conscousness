"""Component determining whether the system is in a state fit for reasoning."""


class ReadinessAssessor:
    """Current implementation always returns ready – expand with health checks."""

    def ready(self) -> bool:
        """Return True if the agent may proceed with reasoning steps."""
        # Placeholder for more complex readiness logic (rate-limiting, resource monitoring…)
        return True