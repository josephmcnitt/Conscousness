"""Passive component responsible for capturing and pre-processing input stimuli."""


class DeepListener:
    """Stub implementation – extend with NLP pipelines / speech-to-text etc."""

    def listen(self, stimulus: str) -> str:
        """For now we simply return the raw stimulus, acting as a passthrough."""
        # Future: add sentiment analysis, context enrichment, etc.
        return stimulus