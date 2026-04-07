class Car:
    def __init__(self, plateNumber, xLocation=0, yLocation=0, speed=0):
        self.plateNumber = plateNumber
        self.xLocation = xLocation
        self.yLocation = yLocation
        self.speed = speed

    def move(self, dx, dy):
        self.xLocation += dx
        self.yLocation += dy
        print(f"Car {self.plateNumber} moved to ({self.xLocation}, {self.yLocation})")

    def park(self):
        self.speed = 0
        print(f"Car {self.plateNumber} is parked at ({self.xLocation}, {self.yLocation})")

    def accelerate(self, ds):
        self.speed += ds
        print(f"Car {self.plateNumber} accelerated to {self.speed} km/h")

car1 = Car("ABC123")
car1.accelerate(50)   # increase speed by 50 km/h
car1.move(10, 0)      # Move 10 units along the x-axis
car1.park()           # Park the car