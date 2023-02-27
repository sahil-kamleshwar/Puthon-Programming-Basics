#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

class vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

    def drive(self, speed):
        self.mode="driving"
        self.speed=speed

class car(vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheels=4
        self.doors=4
        self.enginetype=enginetype

    def drive(self, speed):
        super().drive(speed)
        print("driving my", self.enginetype, "car at", self.speed)
    
class motorcycle(vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcycle")
        if(hassidecar):
            self.wheels=3
        else:
            self.wheels=2
        self.doors=0
        self.enginetype=enginetype

    def drive(self, speed):
        super().drive(speed)
        print("driving my", self.enginetype, "motorcycle at", self.speed)
    
car1=car("gas")
car2=car("electric")
mc1=motorcycle("gas", True)

print(mc1.wheels)
print(car1.enginetype)
print(car2.doors)

car1.drive(30)
car2.drive(40)
mc1.drive(59)