from robot3 import Robot3
import time


class Robot3Behavior:
    def __init__(self, the_robot):
        self.robot = the_robot
        self.angle = 0
        self.forward_dist = 15
        self.right_dist = 15
        self.left_dist = 15
        self.angle_distance = [[90,0],[0,0],[-90,0]]
        self.stopinng_distance_in = 20
    
    def set_pan_start(self):
        self.angle = 0
        self.robot.set_pan(self.angle)
    
    def find_forward_dist(self):
        self.angle = 0
        #self.angle_distance[1][0] = self.angle
        self.angle_distance[1][1] = self.robot.return_distance_at(self.angle)
        #print(self.angle_distance[1][1])
    
    def find_left_dist(self):
        self.angle = 90
        #self.angle_distance[0][0] = self.angle
        self.angle_distance[0][1] = self.robot.return_distance_at(self.angle)
    
    def find_right_dist(self):
        self.angle = -90
        #self.angle_distance[2][0] = self.angle
        self.angle_distance[2][1] = self.robot.return_distance_at(self.angle)
    
    def test_sensor(self):
        test_index = 0
        self.forward_dist()
        while test_index < 20:
            self.find_forward_dist()
            time.sleep(0.5)
            self.find_right_dist()
            time.sleep(0.5)
            self.find_left_dist()
            time.sleep(0.5)
            print(self.angle_distance)
            test_index +=1

    def run_behavior(self, speed):
        self.set_pan_start()
        while True:
            self.find_forward_dist()
            if self.angle_distance[1] < 12:
                self.robot.stop_motors()
                self.find_right_dist()
                if self.angle_distance[1] > 12:
                    self.robot.turn_right(speed)
                    time.sleep(0.5)
                elif self.angle_distance[1] < 12:
                    self.find_left_dist()
                    if self.angle_distance[1] < 12:
                        self.robot.go_backwards(speed)
                        time.sleep(0.5)
                    elif self.angle_distance[1] > 12:
                        self.robot.turn_left(speed)
                        time.sleep(0.5)
            else:
                self.robot.go_straight(speed)
                time.sleep(0.5)
    
    def run2(self, speed):
        self.set_pan_start()
        while True:
            self.find_forward_dist()
            time.sleep(0.02)
            self.find_right_dist()
            time.sleep(0.02)
            self.find_left_dist()
            time.sleep(0.02)
            print(self.angle_distance)
            if self.angle_distance[1][1] < self.stopinng_distance_in:
                self.robot.stop_motors()
                time.sleep(0.02)
                if self.angle_distance[2][1] > self.stopinng_distance_in:
                    self.robot.turn_right(speed)
                elif self.angle_distance[2][1] < self.stopinng_distance_in:
                    if self.angle_distance[0][1] > self.stopinng_distance_in:
                        self.robot.turn_left(speed)
                    elif self.angle_distance[0][1] < self.stopinng_distance_in:
                        self.robot.go_backwards(speed)
                        time.sleep(0)
                        
            else:
                self.robot.go_straight(speed)
    
    def run3(self, speed):
        #self.set_pan_start()
        self.find_forward_dist()
        time.sleep(0.5)
        self.find_right_dist()
        time.sleep(0.5)
        self.find_left_dist()
        time.sleep(0.5)
        sleepy = 0.4
        print(self.angle_distance)
        while True:
            self.find_forward_dist()
            time.sleep(sleepy)
            self.find_right_dist()
            time.sleep(sleepy)
            self.find_left_dist()
            time.sleep(sleepy)
            self.find_forward_dist()
            print(self.angle_distance)
            if (self.angle_distance[1][1] > self.stopinng_distance_in):
                self.robot.go_straight(speed)
                print('going forward...')
            elif (self.angle_distance[0][1] > self.stopinng_distance_in):
                self.robot.turn_left(speed)
                print('turning left...')
            elif (self.angle_distance[2][1] > self.stopinng_distance_in):
                self.robot.turn_right(speed)
                print('turn right...')
            else:
                self.robot.stop_all()
                print('stopping...')
            
            


bot = Robot3()
behavior = Robot3Behavior(bot)
#behavior.run3(40)
behavior.test_sensor()

    