#keyboard.py

'''import robot3
from Raspi_MotorHAT import Raspi_MotorHAT
from swiveling import Swivel
from super_sonic import SuperSonic
from robot_imu import RobotImu
import threading'''
import time, atexit
import os
import asyncio
#import msvcrt

speed = 20

key = 'status'
print('\n--------------------------------------------')
print("| Press ESC or CTRL+C if you want to quit. |")
print('--------------------------------------------')
#print('\u0414\u0430\u0432\u0438\u043D') #name in Cyrillic using UTF-8 code
print("\nБаттерБот/ButterBot\n\nMode: Manual\n")

'''Create print statements that explains keys to control robot...'''

def getchar():
	# Returns a single character from standard input
	ch = ''
	#Only useful for if the machine this runs on *might* be a MS Windows machine
	'''if os.name == 'nt': # how it works on windows
		ch = msvcrt.getch()
	else:'''
	import tty, termios, sys
	fd = sys.stdin.fileno()
	old_settings = termios.tcgetattr(fd)
	try:
		tty.setraw(sys.stdin.fileno())
		ch = sys.stdin.read(1)
	finally:
		termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
	if ord(ch) in [3, 27]: quit() # handle ctrl+C
	return ch

'''while 1:
	ch = getchar()
	print('You pressed %c (%i)' % (ch, ord(ch)))
	if ord(ch) == 62:
			if speed < 100:
				speed +=10
				print('speed:', speed)'''


def keyboard_control():
	while True:
		global speed
		key = getchar()
		if ord(key) == 62:
			if speed < 100:
				speed += 10
				print('Speed:', speed)
		if ord(key) == 60:
			if speed >= 10:
				speed -= 10
				print('Speed:', speed)
		if key == 'w':
			print('Going forward...')
		if key == 'a':
			print('Turning left...')
		if key == 's':
			print('Backing up...')
		if key == 'd':
			print('Turning right...')	
		if key == 'q':
			print('Pivoting left...')
		if key == 'e':
			print('Pivoting right...')
keyboard_control()