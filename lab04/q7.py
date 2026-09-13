class CyberAgent:
    def __init__(self,name,status,threat_score):
        self.name = name
        self.status = status
        self.__threat_score = threat_score

    def updateScore(self,newScore):
        self.__threat_score = newScore

    def getScore(self):
        return self.__threat_score

class NetworkAgent(CyberAgent):
    def analyze(self):
        print(self.name,"analyzing network traffic")

    def respond(self):
        if self.getScore() != 0:
            print(self.name,"responding to network traffic")
        else:
            print("no threats found")

class MalwareAgent(CyberAgent):
    def analyze(self):
        print(self.name,"analyzing malicious activities")

    def respond(self):
        if self.getScore() != 0:
            print(self.name,"responding to malicious activities")
        else:
            print("no threats found")

class IncidentResponseAgent(CyberAgent):
    def analyze(self):
            print(self.name,"analyzing incident responses")

    def respond(self):
        if self.getScore() != 0:
            print(self.name,"responding to incident responses")
        else:
            print("no threats found")


agent1 = MalwareAgent("MalwareAgent","Active",7)
agent2 = NetworkAgent("NetworkAgent","Active",5)
agent3 = IncidentResponseAgent("IncidentResponseAgent","Active",0)
agent1.analyze()
agent1.respond()
agent2.analyze()
agent2.respond()
agent3.analyze()
agent3.respond()
agent1.updateScore(0)
agent2.analyze()
agent1.respond()