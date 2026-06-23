import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import paho.mqtt.publish as publish
import random
import time
import json
from config import MQTT_BROKER, MQTT_PORT, MQTT_TOPIC

# 🔥 MULTIPLE DEVICES
DEVICES = ["ESP32_1", "ESP32_2", "ESP32_3"]

print("🚀 ESP32 Multi-Device Simulator Started...")

while True:
    try:
        for device in DEVICES:

            # 🔥 Realistic sensor value
            value = random.randint(20, 100)

            # 🔥 Simulate anomaly spike occasionally
            if random.random() < 0.3:   # 30% chance
                value = random.randint(80, 100)

            payload = {
                "device_id": device,
                "value": value,
                "timestamp": time.strftime("%H:%M:%S")
            }

            message = json.dumps(payload)

            publish.single(
                MQTT_TOPIC,
                message,
                hostname=MQTT_BROKER,
                port=MQTT_PORT
            )

            print(f"📡 {device} → {message}")

        time.sleep(2)

    except Exception as e:
        print("❌ Error sending data:", e)
        time.sleep(5)