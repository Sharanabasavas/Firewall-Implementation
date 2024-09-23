class RuleManager:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        if rule not in self.rules:
            self.rules.append(rule)
            print(f"Added rule: {rule}")
        else:
            print(f"Rule already exists: {rule}")

    def remove_rule(self, rule):
        if rule in self.rules:
            self.rules.remove(rule)
            print(f"Removed rule: {rule}")
        else:
            print(f"Rule not found: {rule}")

    def list_rules(self):
        if not self.rules:
            print("No rules defined.")
        else:
            print("Active firewall rules:")
            for rule in self.rules:
                print(rule)
