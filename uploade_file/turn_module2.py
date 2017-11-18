######################################################################
# 20171618 Dong_Seola 's code
# 2017. 10. 30
# this swing_point_turn.py file is
# to control raspberry car's truning
######################################################################

# =======================================================================
# import GPIO library and time module
# =======================================================================

import RPi.GPIO as GPIO
import time

# ======================================================================
# import setup_base to get pins and True or False
# The motor set to go
# The import motor module to move
# ======================================================================
import setup_base

# =======================================================================
# perform right swing turn of 90 degree
# Turn right with left motor(go forward)
# =======================================================================

def SwingTurn(speed, running_time):

    # set the left motor and pwm to go forwrard
    setup_base.motor(setup_base.forward0, setup_base.Motor_Left_A, setup_base.Motor_Left_B)
    GPIO.output(setup_base.Motor_Left_PWM, GPIO.HIGH)

    # set the right motor pwm to stop = turn off
    GPIO.output(setup_base.Motor_Right_PWM, GPIO.LOW)

    # set the speed of the left motor to go forward
    setup_base.Left_Pwm.ChangeDutyCycle(speed)
    # set the speed of the right motor to stop
    setup_base.Right_Pwm.ChangeDutyCycle(0)

    # set the running time of the left motor to go forward
    time.sleep(running_time)

# =======================================================================
# perform left swing turn of 90 degree
# Turn left with right motor(go forward)
# =======================================================================

def left_SwingTurn(speed, running_time):

    # set the left motor pwm to stop = turn off
    GPIO.output(setup_base.Motor_Left_PWM, GPIO.LOW)

    # set the right motor and pwm to go forward
    setup_base.motor(setup_base.forward0, setup_base.Motor_Right_A, setup_base.Motor_Right_B)
    GPIO.output(setup_base.Motor_Right_PWM, GPIO.HIGH)

    # set the speed of the left motor to stop
    setup_base.Left_Pwm.ChangeDutyCycle(0)
    # set the spedd of the right motor to go forward
    setup_base.Right_Pwm.ChangeDutyCycle(speed)

    # set the running tiem of the right motor to go forward
    time.sleep(running_time)

# =======================================================================
# perform right point turn of 90 degree
# Turn right with left motor(forward) and right motor(backward)
# ======================================================================

def right_PointTurn(speed, running_time):

    # set the left motor and pwm to go forward
    setup_base.motor(setup_base.forward0, setup_base.Motor_Left_A, setup_base.Motor_Left_B)
    GPIO.output(setup_base.Motor_Left_PWM, GPIO.HIGH)

    # set the right motor and pwm to go backward
    setup_base.motor(setup_base.backward1, setup_base.Motor_Right_A, setup_base.Motor_Right_B)
    GPIO.output(setup_base.Motor_Right_PWM, GPIO.LOW)

    # set the speed of the left and right motor to go
    setup_base.Left_Pwm.ChangeDutyCycle(speed)
    setup_base.Right_Pwm.ChangeDutyCycle(speed)

    # set the running time of the left and right motor
    time.sleep(running_time)

#=======================================================================
# perform left point turn of 90 degree
# Turn left with right motor(forward) and left motor(backward)
# ======================================================================

def left_PointTurn(speed, running_time):

    # set the left motor and pwm to go backward
    setup_base.motor(setup_base.bakward0, setup_base.Motor_Left_A, setup_base.Motor_Left_B)
    GPIO.output(setup_base.Motor_Left_PWM, GPIO.LOW)

    # set the right motor and pwm to go forward
    setup_base.motor(setup_base.forward1, setup_base.Motor_Right_A, setup_base.Motor_Right_B)
    GPIO.output(setup_base.Motor_Right_PWM, GPIO.HIGH)

    # set the speed of the left and right motor to go
    setup_base.Left_Pwm.ChangeDutyCycle(speed)
    setup_base.Right_Pwm.ChangeDutyCycle(speed)

    # set the running time of the left and right motor
    time.sleep(running_time)