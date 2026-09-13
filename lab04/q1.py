class ThreatDetector:
    def __init__(self, device_name, ip_address, threat_level):
        self.device_name = device_name
        self.ip_address = ip_address
        self.threat_level = threat_level
    def scan(self):
        print("\nSecurity System")
        print("Device Name: ", self.device_name)
        print("IP Address: ", self.ip_address)
        print("Threat Level: ", self.threat_level)
        if self.threat_level == "Low":
            print("System Response: System Safe")
        elif self.threat_level == "Medium":
            print("System Response: Suspicious Activity")
        elif self.threat_level == "High":
            print("System Response: Criticsl Threat Detected")

dev1 = ThreatDetector("phone","100.200.3.40", "Low")
dev2 = ThreatDetector("ipad","130.600.3.70", "Medium")
dev3 = ThreatDetector("laptop","140.400.3.80", "High")

dev1.scan()
dev2.scan()
dev3.scan()