import json
import paho.mqtt.client as mqtt

from config import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC
from analyzer.risk_engine import calculate_risk
from analyzer.device_tracker import update_device


def on_connect(client, userdata, flags, rc):
    print("✅ Connected to MQTT Broker")
    client.subscribe(MQTT_TOPIC)


def detect_anomaly(device, traffic):

    update_device(device)

    if traffic > 150:
        calculate_risk("Network DDoS", device, traffic)

    elif traffic > 90:
        calculate_risk("Suspicious Activity", device, traffic)

    elif traffic > 50:
        calculate_risk("Anomaly Detected", device, traffic)

    else:
        calculate_risk("Normal Activity", device, traffic)


def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())

        device = data["device_id"]
        traffic = data["traffic"]

        print(f"📡 {device} → {traffic}")

        detect_anomaly(device, traffic)

    except Exception as e:
        print("Error:", e)


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT, 60)
client.loop_forever()