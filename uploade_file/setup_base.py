#########################################################################
# 20171618 Dong-Seola(동설아)
# 2017. 10. 30.
# This code is basic code to set by Raspberry(car)
#########################################################################

# =======================================================================
# import GPIO library module
# =======================================================================

import RPi.GPIO as GPIO

def base_setup() :
    # =======================================================================
    # Set the motor's true / false value to go forward.
    # Set the motor's true / false value to go opposite(backward).
    # =======================================================================

    forward0 = True
    forward1 = False
    backward0 = not forward0
    backward1 = not forward1

    # =======================================================================
    # declare the pins of 12, 11, 35 in the Rapberry Pi
    # as the left motor control pins in order to control left motor
    # left motor needs three pins to be controlled
    # =======================================================================

    Motor_Left_A = 12
    Motor_Left_B = 11
    Motor_Left_PWM = 35

    # =======================================================================
    # declare the pins of 15, 13, 37 in the Rapberry Pi
    # as the right motor control pins in order to control right motor
    # right motor needs three pins to be controlled
    # =======================================================================

    Motor_Right_A = 15
    Motor_Right_B = 13
    Motor_Right_PWM = 37

    # =======================================================================
    # set Both wheel to move by GPIO
    # =======================================================================

    GPIO.setup(Motor_Left_A,GPIO.OUT)
    GPIO.setup(Motor_Left_B,GPIO.OUT)
    GPIO.setup(Motor_Left_PWM,GPIO.OUT)

    GPIO.setup(Motor_Right_A,GPIO.OUT)
    GPIO.setup(Motor_Right_B,GPIO.OUT)
    GPIO.setup(Motor_Right_PWM,GPIO.OUT)

    # =======================================================================
    # create left and right pwm object to control the speed of left motor
    # The speed is between 0 and 100
    # =======================================================================

    Left_Pwm=GPIO.PWM(MotorLeft_PWM,100)
    Right_Pwm=GPIO.PWM(MotorRight_PWM,100)

# ===========================================================================
# Control the DC motor to make it rotate clockwise,
# so the car will move
# ===========================================================================

def motor(x, Motor_A, Motor_B):
    # if motor is left -> try 0(forward, backward)
    # if motor is right -> try 1(forward, backward)
    if x == 'True':
        GPIO.output(Motor_A, GPIO.HIGH)
        GPIO.output(Motor_B, GPIO.LOW)
    elif x == 'False':
        GPIO.output(Motor_A, GPIO.LOW)
        GPIO.output(Motor_B, GPIO.HIGH)
    else:
        print('Config Error')

