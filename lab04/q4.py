class Robot:
    def __init__(self, name, battery):
        self.name = name
        self.battery = battery
    def move(self):
        if self.battery > 20:
            print("Moving")
        else:
            print("Battery level is below 20%")
    def charge(self):
        self.battery = 100
        print("100% charged")
class DeliveryRobot(Robot):
    def move(self):
        if self.battery > 20:
            print("Moving to delivery location")
        else:
            print("Battery level is below 20%")
class SecurityRobot(Robot):
    def move(self):
        if self.battery > 20:
            print("Patrolling a specific area")
        else:
            print("Battery level is below 20%")
class RescueRobot(Robot):
    def move(self):
        if self.battery > 20:
            print("Moving towards a disaster location")
        else:
            print("Battery level is below 20%")
rob1 = DeliveryRobot("panda", 20)
rob1.move()
rob1.charge()
rob1.move()
rob2 = DeliveryRobot("junior", 80)
rob2.move()
rob3 = RescueRobot("kiwi", 100)
rob3.move()