#test_motors.py

from Raspi_MotorHAT import Raspi_MotorHAT
from gpiozero import DistanceSensor
from servo import Servo

import time, atexit

class Robot2(object):
    def __init__(self, motorhat_addr=0x6f):
        #setup the motorhat with the passed in address
        self._mh = Raspi_MotorHAT(addr=motorhat_addr)

        #get local variable for each motor upto 4
        self.fL = self._mh.getMotor(1)
        self.fR = self._mh.getMotor(2)
        self.bL = self._mh.getMotor(3)
        self.bR = self._mh.getMotor(4)

        #setup the distance sensors
        #self.left_distance_sensor = DistanceSensor(echo=17, trigger=27, queue_len=2)
        #self.right_distance_sensor = DistanceSensor(echo=5, trigger=6, queue_len=2)

        self.distance_sensor = DistanceSensor(echo=17, trigger=27, queue_len=1)
        self.dist_off = 100/2.54

        # set up servo
        self.servo = Servo(addr=motorhat_addr)

        #make sure motors stop when code exits
        
        atexit.register(self.stop_motors)

    #convert speed & mode
    def convert_speed(self, speed):
        #choose the running mode
        mode = Raspi_MotorHAT.RELEASE
        if speed > 0:
            mode = Raspi_MotorHAT.FORWARD
        elif speed < 0:
            mode = Raspi_MotorHAT.BACKWARD
        
        #Scale the speed 
        output_speed = (abs(speed) * 255) // 100
        return mode, int(output_speed)
    
    #use speed conversion to change motor movements
    def set_front_left(self, speed):
        mode, output_speed = self.convert_speed(speed)
        self.fL.setSpeed(output_speed)
        self.fL.run(mode)
    def set_back_left(self, speed):
        mode, output_speed = self.convert_speed(speed)
        self.bL.setSpeed(output_speed)
        self.bL.run(mode)
    def set_front_right(self, speed):
        mode, output_speed = self.convert_speed(speed)
        self.fR.setSpeed(output_speed)
        self.fR.run(mode)
    def set_back_right(self, speed):
        mode, output_speed = self.convert_speed(speed)
        self.bR.setSpeed(output_speed)
        self.bR.run(mode)

    #define a moveset
    def go_straight(self, speed):
        """set all wheels going forward with
        same speed"""
        self.set_front_left(speed)
        self.set_front_right(speed)
        self.set_back_left(speed)
        self.set_back_right(speed)
    
    def go_backwards(self, speed):
        """set all wheels going backwards with
        same speed"""
        speed = -speed
        self.set_front_left(speed)
        self.set_front_right(speed)
        self.set_back_left(speed)
        self.set_back_right(speed)

    def turn_left(self, speed):
        """'normal' leftwards turn"""
        self.set_front_left(speed)
        self.set_front_right(speed/2)
        self.set_back_left(speed)
        self.set_back_right(speed/2)
    
    def turn_right(self, speed):
        """'normal' rightwards turn"""
        self.set_front_left(speed/2)
        self.set_front_right(speed)
        self.set_back_left(speed/2)
        self.set_back_right(speed)

    # define different movesets

    #stop motors
    def stop_motors(self):
        """stops all the wheels"""
        self.fL.run(Raspi_MotorHAT.RELEASE)
        self.fR.run(Raspi_MotorHAT.RELEASE)
        self.bL.run(Raspi_MotorHAT.RELEASE)
        self.bR.run(Raspi_MotorHAT.RELEASE)
    
    def stop_all(self):
        self.stop_motors()
        
    
    def set_pan(self, position):
        """Might be replaced by Swivel class
        Will be working in degrees/radians so position of objects can 
        actually be determined by the robot
        Such as 90-180 being on the left side.. and therefore it would turn right"""
        if position == 'mid':
            self.servo.set_to_mid()
            time.sleep(0.2)
            self.display_distance()
        if position == 'left':
            self.servo.set_to_max()
            time.sleep(0.2)
            self.display_distance()
        if position == 'right':
            self.servo.set_to_min()
            time.sleep(0.2)
            self.display_distance()

    def display_distance(self):
        print('Distance: {s}'.format(s=self.distance_sensor.distance*self.dist_off))

    def return_distance(self):
        return self.distance_sensor.distance*self.dist_off

