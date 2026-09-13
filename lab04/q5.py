class Agent:
    def __init__(self, name, status):
        self.name = name
        self.status = status
    def perform_task(self):
        print("Performing task")
class SecurityAgent(Agent):
    def perform_task(self):
        print("Detecting cyber threat")
class MonitoringAgent(Agent):
    def perform_task(self):
        print("Monitoring system activity")
class RecoveryAgent(Agent):
    def perform_task(self):
        print("Recovering system services")

agent1 = SecurityAgent("Jane", "Active")
agent2 = MonitoringAgent("Professor", "Active")
agent3 = RecoveryAgent("Dr Strange", "Active")
agent1.perform_task()
agent2.perform_task()
agent3.perform_task()