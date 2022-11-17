from servo import Servo
import time
from gpiozero import DistanceSensor

sensor = DistanceSensor(echo=17, trigger=27, queue_len=2)


servo1 = Servo()

sleeptime = 1.5
dist_off = 100/2.54

while True:
    servo1.set_to_mid()
    time.sleep(sleeptime)
    print('Front: {s}'.format(s=sensor.distance*dist_off))
    servo1.set_to_min()
    time.sleep(sleeptime)
    print('Right: {s}'.format(s=sensor.distance*dist_off))
    servo1.set_to_mid()
    time.sleep(sleeptime)
    print('Front: {s}'.format(s=sensor.distance*dist_off))
    servo1.set_to_max()
    time.sleep(sleeptime)
    print('Left: {s}'.format(s=sensor.distance*dist_off))



