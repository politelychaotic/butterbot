from time import sleep
import time
import math
from robot3 import Robot3
import threading

class ArcPanBehavior:
    def __init__(self, the_robot):
        self.robot = the_robot
        self.current_time = 0
        self.frames_per_half_circle = 50
        self.radians_per_frame = (2*math.pi) / self.frames_per_half_circle
        self.radius = 90
        self.frame_in_radians = 0
        self.stopping_distance_in = 10
        self.right = 0
        self.front = 0
        self.left = 0
        self.distances = {
            "Front: " : [0,],
            "Right: " : [0,],
            "Left: " : [0,]
        }

    def return_angle(self):
        return (self.radius * math.cos(self.frame_in_radians))
    
    def run(self):
        timeout = time.time() + 6
        while True:
            frame_number = self.current_time % self.frames_per_half_circle
            self.frame_in_radians = frame_number * self.radians_per_frame
            self.robot.set_pan(self.radius * math.cos(self.frame_in_radians))
            angle = self.return_angle()
            if (angle >= 89):
                self.front = self.robot.return_distance()
                front = self.front
                self.distances["Front"] = front
                print("Front distance: ", front, angle)
            if(angle >= -16 and angle <= 16):
                self.left = self.robot.return_distance()
                left = self.left
                self.distances["Left"] = left
                print("Left distance: ", left, angle)
            if(angle <= -89):
                self.right = self.robot.return_distance()
                right = self.right
                self.distances["Right"] = right
                print("Right distance: ", right, angle)
            if time.time() > timeout:
                break

            sleep(0.05)
            self.current_time += 1
    def move(self, speed):
        while True:
            self.run()
            if(self.front > self.stopping_distance_in):
                self.robot.go_straight(speed)
                print("Going forward...")
            elif(self.left > self.stopping_distance_in):
                self.robot.turn_right(speed)
                print("Turning left...")
            elif(self.right > self.stopping_distance_in):
                self.robot.turn_left(speed)
                print("Turning right...")
            else:
                self.robot.stop_all()
                print("Stopping...")

    '''def start(self):
        threadOne = threading.Thread(target=self.run())
        threadOne.start()
        threadTwo = threading.Thread(target=self.move())
        threadTwo.start()'''

'''class FuncThread(threading.Thread):
    def __init__(self, target, *args):
        self._target = target
        self._args = args
        threading.Thread.__init__(self)

    def run(self):
        self._target()

threadOne = FuncThread(behavior.run())
behavior.move()
threadOne.join()'''

bot = Robot3()
behavior = ArcPanBehavior(bot)
#behavior.run()
behavior.move(20)




'''
bot.set_pan(0)
print(bot.return_distance_at(-90))
print(bot.get_dist_angle_list())
print(bot.return_distance_at(0))
print(bot.get_dist_angle_list())
print(bot.return_distance_at(90))
print(bot.get_dist_angle_list())
'''