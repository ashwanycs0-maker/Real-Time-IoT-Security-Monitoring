import random
from analyzer.risk_engine import calculate_risk

def detect_anomaly(device, value):

    value = random.randint(0,100)

    if value > 70:   # 🔥 lower for demo
        calculate_risk("Anomaly Detected", device, value)