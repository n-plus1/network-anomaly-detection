from scapy.all import sniff, wrpcap

# Replace with the correct interface GUID from your find_interface.py output
INTERFACE_GUID = r"\Device\NPF_{705FE8B9-29C8-43E9-8E13-13A8970A594F}"

def start_capture(interface=INTERFACE_GUID, count=100, output_file="vm_traffic.pcap"):
    print(f"Starting capture on {interface}...")
    
    packets = sniff(
        iface=interface,
        count=count,
        store=True
    )
    
    wrpcap(output_file, packets)
    print(f"Saved {len(packets)} packets to {output_file}")

if __name__ == "__main__":
    start_capture()