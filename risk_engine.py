from analyzer.alert_logger import log_alert
from datetime import datetime

last_alert_time = {}

def calculate_risk(alert_type, source, value=0):

    current_time = datetime.now()

    if "DDoS" in alert_type:
        risk = "HIGH"
    elif "Suspicious" in alert_type or "Anomaly" in alert_type:
        risk = "MEDIUM"
    else:
        risk = "NORMAL"

    # ✅ 1 alert per 8 sec per device
    if source not in last_alert_time or (current_time - last_alert_time[source]).seconds > 8:
        last_alert_time[source] = current_time
        log_alert(alert_type, source, risk, value)

    return risk