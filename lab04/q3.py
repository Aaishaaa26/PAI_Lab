class SecuritySystem:
    def respond(self):
        print("Security System Respond")
class Firewall(SecuritySystem):
    def respond(self):
        print("Firewall: Block Suspicious Network Traffic")
class Antivirus(SecuritySystem):
    def respond(self):
        print("Antivirus: Isolate malicious files")
class IntrusionDetectionSystem(SecuritySystem):
    def respond(self):
        print("Intrusion Detection System: Generate Security ALert")

system1 = Firewall()
system2 = Antivirus()
system3 = IntrusionDetectionSystem()
system1.respond()
system2.respond()
system3.respond()