class Device:
    def __init__(self, device_id, model):
        self.device_id = device_id
        self.model = model

    def display_info(self):
        print(f"Device ID: {self.device_id}")
        print(f"Model: {self.model}")
class Flyer:
    def fly(self):
        print("The drone is flying...")
class Drone(Device, Flyer):
    def __init__(self, device_id, model):
        super().__init__(device_id, model)

    def capture_image(self):
        print("Image captured by the drone.")
drone1 = Drone("DRN001", "Phantom-X")
drone1.display_info()       
drone1.fly()                
drone1.capture_image()      