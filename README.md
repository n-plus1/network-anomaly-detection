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
- **Reasoning:** Complete isolation from physical network to prevent attack traffic from escaping the lab environment. Follows defense-in-depth principles.
- **IP Scheme:** [Will be filled after configuration]
