from robot2 import Robot2
import time


#servo1 = Servo()
robot = Robot2()
sp = 25
sleeptime = 0.5
#robot.go_straight(sp)
front_dist = 15
left_dist = 15
right_dist = 15



        
            

'''
while True:
    robot.set_pan('mid')
    front_dist = robot.return_distance()
    if front_dist <= 12.0:
        robot.stop_motors()
        robot.go_backwards(sp)
        front_dist = robot.return_distance()
        if front_dist > 12:
            robot.turn_right(sp)
    time.sleep(sleeptime)
    robot.set_pan('right')
    right_dist = robot.return_distance()
    if right_dist <= 12.0:
        robot.turn_left(sp)
    time.sleep(sleeptime)
    robot.set_pan('left')
    left_dist = robot.return_distance()
    if left_dist <= 12.0:
        robot.turn_right(sp)
    time.sleep(sleeptime)'''
