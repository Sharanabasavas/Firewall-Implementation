import unittest
from src.rule_manager import RuleManager

class TestFirewall(unittest.TestCase):
    def setUp(self):
        self.rule_manager = RuleManager()

    def test_add_rule(self):
        rule = "-A INPUT -p tcp --dport 80 -j ACCEPT"
        self.rule_manager.add_rule(rule)
        self.assertIn(rule, self.rule_manager.rules)

    def test_remove_rule(self):
        rule = "-A INPUT -p tcp --dport 80 -j ACCEPT"
        self.rule_manager.add_rule(rule)
        self.rule_manager.remove_rule(rule)
        self.assertNotIn(rule, self.rule_manager.rules)

if __name__ == "__main__":
    unittest.main()
