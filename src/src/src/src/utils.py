import logging

# Configure logging
logging.basicConfig(filename='../logs/firewall.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def log_traffic(message):
    logging.info(message)

def log_blocked_traffic(packet):
    logging.warning(f"Blocked packet: {packet}")
