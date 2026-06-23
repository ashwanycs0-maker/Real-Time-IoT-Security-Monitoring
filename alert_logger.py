import json
import os
from datetime import datetime

LOG_FILE = "logs/alerts.json"

os.makedirs("logs", exist_ok=True)

def get_alerts():
    try:
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def log_alert(alert_type, source, risk, value):

    alert = {
        "time": datetime.now().strftime("%H:%M:%S"),
        "type": alert_type,
        "source": source,
        "risk": risk,
        "value": value
    }

    if os.path.exists(LOG_FILE):
        try:
            with open(LOG_FILE, "r") as f:
                data = json.load(f)
        except:
            data = []
    else:
        data = []

    data.append(alert)

    # ✅ Keep last 100 alerts (stable UI)
    if len(data) > 100:
        data = data[-100:]

    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=4)