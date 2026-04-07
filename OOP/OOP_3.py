class SoccerPlayer:
    def __init__(self, name, number, xLocation=0, yLocation=0):
        self.name = name
        self.number = number
        self.xLocation = xLocation
        self.yLocation = yLocation

    def run(self, dx, dy):
        self.xLocation += dx
        self.yLocation += dy
        print(f"{self.name} ran to ({self.xLocation}, {self.yLocation})")

    def jump(self):
        print(f"{self.name} jumped!")

    def kickBall(self):
        print(f"{self.name} kicked the ball!")


player1 = SoccerPlayer("Bob", 10)
player1.run(5, 3)  # Bob run to (5, 3)
player1.jump()      # Bob jumped!
player1.kickBall()  # Bob kicked the ball!