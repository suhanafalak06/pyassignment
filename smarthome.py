class Appliance:
    def status(self):
        print("Appliance status is unknown.")
class Fan(Appliance):
    def status(self):
        print("Fan is spinning at medium speed.")
class Light(Appliance):
    def status(self):
        print("Light is turned on with warm white brightness.")
class AC(Appliance):
    def status(self):
        print("AC is cooling at 22°C in auto mode.")
devices = [Fan(), Light(), AC()]
for device in devices:
    device.status()