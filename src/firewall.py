import os
import subprocess
from rule_manager import RuleManager

class Firewall:
    def __init__(self):
        self.rules = RuleManager()

    def add_rule(self, rule):
        """
        Add a rule to iptables/nftables.
        """
        command = f"sudo iptables {rule}"  # or replace with nftables command
        self._execute_command(command)
        self.rules.add_rule(rule)

    def remove_rule(self, rule):
        """
        Remove a rule from iptables/nftables.
        """
        command = f"sudo iptables {rule}"  # or replace with nftables command
        self._execute_command(command)
        self.rules.remove_rule(rule)

    def list_rules(self):
        """
        List all current iptables rules.
        """
        self.rules.list_rules()

    def _execute_command(self, command):
        """
        Helper to execute shell commands.
        """
        try:
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error executing command: {e}")

if __name__ == "__main__":
    firewall = Firewall()
    # Example usage:
    firewall.add_rule("-A INPUT -p tcp --dport 22 -j ACCEPT")  # Allow SSH traffic
    firewall.list_rules()
