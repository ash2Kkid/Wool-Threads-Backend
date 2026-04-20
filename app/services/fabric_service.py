import random

PATTERNS = ["striped", "solid", "printed", "lattice"]
QUALITIES = ["good", "bad"]

def analyze_fabric_mock():
    return {
        "pattern": random.choice(PATTERNS),
        "quality": random.choice(QUALITIES),
        "confidence": round(random.uniform(0.7, 0.95), 2)
    }