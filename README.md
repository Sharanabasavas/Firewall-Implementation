# Firewall Application

## Overview
This project implements a basic firewall application that filters incoming and outgoing network traffic using `iptables` or `nftables` in Python. Additionally, a low-level packet filtering example in C is included.

### Features
- Add, remove, and list firewall rules using `iptables` or `nftables`.
- Low-level packet filtering using C and `libpcap`.
- Logging of traffic and blocked packets.

## Technologies Used
- **Python**: High-level management of firewall rules.
- **C**: For low-level packet inspection and filtering.
- **iptables/nftables**: Linux networking tools for firewall configuration.
- **libpcap**: Library
### Running the Firewall
1. **Add a firewall rule**:
    ```
    python src/firewall.py
    ```

2. **Example commands**:
    - Add a rule to accept SSH traffic:
      ```bash
      firewall.add_rule("-A INPUT -p tcp --dport 22 -j ACCEPT")
      ```

    - List all current rules:
      ```bash
      firewall.list_rules()
      ```

    - Remove a rule:
      ```bash
      firewall.remove_rule("-D INPUT -p tcp --dport 22 -j ACCEPT")
      ```

### Running Unit Tests
To run unit tests for rule management:
 for network packet capture.

## Setup Instructions

### Prerequisites
- Python 3.x
- A Linux-based system with `iptables` or `nftables` installed.
- `gcc` for compiling C code.
- `libpcap` installed.

### Install Python Dependencies

### Compile C Code
To compile the C packet filter:

## License
This project is licensed under the MIT License.

