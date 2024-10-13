from dataclasses import dataclass

@dataclass
class PredictionDto:
    activity: str
    accuracy: float