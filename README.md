# Network Traffic Anomaly Detection System

## Overview
A Python-based network monitoring tool that uses machine learning to detect anomalous traffic patterns in real-time. Built as a security lab project to demonstrate practical application of cybersecurity principles and AI-driven threat detection.

## Author
n-plus1

## Date Started
March 2026

## Lab Environment

### Virtual Machines
| VM Name | Role | OS | Purpose |
|---------|------|-----|---------|
| Kali Linux | Attacker | Debian-based | Generate attack traffic (Nmap, Slowloris, Hydra) |
| Metasploitable 1 | Victim | Ubuntu 8.04 | Vulnerable target for penetration testing |
| Metasploitable 2 | Victim | Ubuntu 8.04 | Redundant target for repeated experiments |

### Virtualization Platform
- **Software:** Windows 11; VMware Workstation Pro 17.x
- **License:** Personal use (lifetime license)
- **Hardware:** CPU - AMD Ryzen 7 7800x3d; GPU - AMD Radeon RX 9070 XT; RAM - 32 GB DDR5 @6000Mhz 

### Network Configuration
- **Mode:** Host-Only (VMnet1)
- **Reasoning:** 
  - **Isolation:** Ensures complete containment of attack traffic. Even if a VM is fully compromised, the attacker cannot reach the physical network, router, or other devices.
  - **Safety:** Follows the principle of defense-in-depth by creating a logical air gap between the lab and the production/home network.
  - **Control:** Allows direct communication between VMs for testing while blocking external egress/ingress.
- **IP Scheme:** 
  - Subnet: 192.168.x.0/24 (Dynamic assignment via VMware DHCP)
  - Gateway: None (No internet access required for this phase)

## Development Progress

### Packet Capture
- **Status:** ✅ Complete
- **Tools:** Scapy (Python library), Npcap (Windows driver)
- **Goal:** Capture network traffic from VMnet1 for ML training
- **Configuration Details:**
  - **Interface:** `\Device\NPF_{705FE8B9-29C8-43E9-8E13-13A8970A594F}` (VMnet1 Host-Only)
  - **Subnet:** 192.168.127.0/24 (VMware Host-Only network)
  - **Verification:** Successfully captured 100 packets containing only VM traffic (Kali ↔ Metasploitable)
- **Notes:** 
  - Initial capture ran on physical network interface (incorrect)
  - Fixed by identifying correct Npcap GUID from `get_if_list()` output
  - Traffic isolation confirmed: No home network traffic leaked into captures
- **Files Added:** 
  - `capture_traffic.py` (packet capture implementation)
  - `find_interface.py` (interface discovery utility)
  - `vm_traffic.pcap` (sample captured traffic)
- **Test Results:** Verified VM traffic capture on correct interface; 100 packets captured during ping test