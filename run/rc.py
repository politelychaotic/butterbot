import curses
from Raspi_MotorHAT import Raspi_MotorHAT
from gpiozero import Robot
from swiveling import Swivel
from super_sonic import SuperSonic
from robot_imu import RobotImu
import threading
from robot3 import Robot3

'''
Basic remote control for robot based on GPIOzero website.
Needs to be modified to accomodate butterbot's 4wd and 
the Raspi_MotorHAT library I am using.
For now this serves as a guideline to adapt into usable 
code later.k
'''

robot = Robot(left=(4,14), right=(17,18)) # WTF is this???????????

speed = 20
inc = 10


actions = {
    curses.KEY_UP:       Robot3.go_straight(speed),
    curses.KEY_DOWN:     Robot3.go_backwards(speed),
    curses.KEY_LEFT:     Robot3.turn_left(speed),
    curses.KEY_RIGHT:    Robot3.turn_right(speed),
    curses.BUTTON_SHIFT: Robot3.return_distance,
    curses.KEY_UP:       Robot3.convert_speed(speed+inc), #new additions
    curses.KEY_DOWN:     Robot3.convert_speed(speed-inc),
}

def main(window):
    next_key = None
    while True:
        curses.halfdelay(1)
        if next_key is None:
            key = window.getch()
        else:
            key = next_key
            next_key = None
        if key != -1: # key pressed
            curses.halfdelay(3)
            action = actions.get(key)
            if action is not None:
                action()
            next_key = key
            if key == curses.KEY_UP:
                speed = speed + inc
            if key == curses.KEY_DOWN:
                speed = speed - inc
            while next_key == key:
                next_key = window.getch()
            # key released
            robot.stop()
curses.wrapper(main)