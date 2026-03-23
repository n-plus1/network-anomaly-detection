from scapy.all import sniff, wrpcap
import os

def packet_callback(packet):
    """Process each captured packet"""
    print(f"Captured: {packet.summary()}")

def start_capture(interface=None, count=100, output_file="traffic.pcap"):
    """
    Start packet capture
    
    Args:
        interface: Network interface to listen on (None = all interfaces)
        count: Number of packets to capture
        output_file: Where to save the PCAP file
    """
    print(f"Starting capture on {interface or 'all interfaces'}...")
    
    packets = sniff(
        iface=interface,
        count=count,
        prn=packet_callback,
        store=True
    )
    
    wrpcap(output_file, packets)
    print(f"Saved {len(packets)} packets to {output_file}")

if __name__ == "__main__":
    # Test capture - adjust interface name as needed
    start_capture(count=50, output_file="test_capture.pcap")