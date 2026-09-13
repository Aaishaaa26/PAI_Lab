class Computer:
    def __init__(self, cpu, ram, battery):
        self.cpu = cpu
        self.ram = ram
        self.battery = battery
    def system_status(self):
        print("\nComputer Status(if any):")
        if self.cpu > 80:
            print("Heavy CPU load")
        if self.ram > 85:
            print("High Memory Usage")
        if self.battery <= 15:
            print("Low Battery")
c1 = Computer(90,70,15)
c1.system_status()
c2 = Computer(50,87,55)
c2.system_status()