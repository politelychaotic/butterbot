
from robot2 import Robot2
from time import sleep

class AvoidObjects:
    def __init__(self, the_robot):
        self.robot = the_robot
        self.speed = 30

    def get_motor_speed(self, distance):
        """choose motor speeds based on distance"""
        if distance < 12:
            self.robot.stop_motors()
            return -self.speed
        else:
            return self.speed
        
    def run(self):
        self.robot.set_pan('mid')
        while True:
            distance = self.robot.return_distance()
            print(distance)
            self.robot.set_front_left(self.get_motor_speed(distance))
            self.robot.set_back_left(self.get_motor_speed(distance))
            self.robot.set_front_right(self.speed)
            self.robot.set_back_right(self.speed)
            sleep(0.5)

bot = Robot2()
behavior = AvoidObjects(bot)
behavior.run()

