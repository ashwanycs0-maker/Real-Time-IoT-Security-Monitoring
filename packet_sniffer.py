from scapy.all import sniff, IP
from analyzer.ddos_detector import detect_ddos
from analyzer.risk_engine import calculate_risk
from analyzer.device_tracker import update_device

packet_count = {}

def process_packet(packet):

    if IP in packet:
        src = packet[IP].src

        packet_count[src] = packet_count.get(src, 0) + 1

        update_device(src)

        # ✅ check every 30 packets (slower)
        if packet_count[src] % 30 == 0:

            print(f"{src} → {packet_count[src]}")

            if detect_ddos(src, packet_count[src]):
                calculate_risk("Network DDoS", src, packet_count[src])
            else:
                calculate_risk("Normal Traffic", src, packet_count[src])

def start_sniffing():
    print("🚀 Sniffing network traffic...")
    sniff(prn=process_packet, store=False)

if __name__ == "__main__":
    start_sniffing()