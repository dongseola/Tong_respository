#forward
#!/usr/bin/env python
# Import necessary modules
import RPi.GPIO as GPIO     #to use GPIO in rasspberry
import video_dir
import car_dir
import motor               #to control motor way and speed
import time                #to control time that motor used

busnum = 1  # Edit busnum to 0, if you uses Raspberry Pi 1 or 0

def find_line(which, strwhich, printwhich ) :
    if line[0:8] == strwhich :
        which = line[11:-1]
        print( printwhich, "=" , which)

#
def setup():
    global offset, offset_x, offset_y, forward0, forward1, backward0, backward1
    offset_x = 0
    offset_y = 0
    offset = 0
    forward0 = 'True'
    forward1 = 'False'

    # Read calibration value from config file
    try:
        for line in open('config'):
            find_line(offset_x, "offset_x", 'offset_x')

            find_line(offset_y, "offset_y", 'offset_y')

            find_line(forward0, "forward0", 'turning0')

            find_line(forward1, "forward1", 'turning1')

            if line[0:8] == 'offset =':
                offset = int(line[9:-1])
                print
                'offset =', offset

    except:
        print
        'no config file, set config to original'

    video_dir.setup(busnum=busnum)
    car_dir.setup(busnum=busnum)
    motor.setup(busnum=busnum)
    video_dir.calibrate(offset_x, offset_y)
    car_dir.calibrate(offset)

    # Set the motor's true / false value to the opposite.
    backward0 = REVERSE(forward0)
    backward1 = REVERSE(forward1)

# Functions to control the direction of motor in reverse
def REVERSE(x):
    if x == 'True':
        return 'False'
    elif x == 'False':
        return 'True'


def go_Forward(speed, running_time):
    global forward0, forward1
    motor.setSpeed(speed)
    motor.motor0(forward0)
    motor.motor1(forward1)
    time.sleep(running_time)
    motor.stop()


def go_Backward(speed, running_time):
    global backward0, backward1
    motor.setSpeed(speed)
    motor.motor0(backward0)
    motor.motor1(backward1)
    time.sleep(running_time)
    motor.stop()


if __name__ == "__main__":
    try:
        setup()
        go_Forward(40, 2)
        time.sleep(1)
        go_Backward(40,2)
        time.sleep(1)
        go_Forward(60, 2)
        time.sleep(1)
        go_Backward(60,2)
        time.sleep(1)
        go_Forward(80, 2)
        time.sleep(1)
        go_Backward(80, 2)
        time.sleep(1)

    except KeyboardInterrupt:
        go_Forward(0, 1)
        quit()