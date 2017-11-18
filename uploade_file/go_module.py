######################################################################
# 20171618 Dong_Seola 's code
# 2017. 10. 30
# this for_back_ward.py file is
# to control raspberry car's go forward and backward
# to motor stop or setup 0
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

setup_base.base_setup()

# =======================================================================
#  go_forward_any method has been generated for the three-wheeled moving
#  objec to go forward without any limitation of running_time
# =======================================================================

def just_go_forward(speed):

    # set left motor to go forward by GPIO and motor_module
    setup_base.motor(setup_base.forward0, setup_base.Motor_Left_A, setup_base.Motor_Left_B)
    GPIO.output(setup_base.Motor_Left_PWM, GPIO.HIGH)

    # set right motor to go forward by GPIO and motor_module
    setup_base.motor(setup_base.forward1, setup_base.Motor_Right_A, setup_base.Motor_Right_B)
    GPIO.output(setup_base.Motor_Right_PWM, GPIO.HIGH)

    # set left and right Pwm to get speed
    setup_base.Left_Pwm.ChangeDutyCycle(speed)
    setup_base.Right_Pwm.ChangeDutyCycle(speed)

# =======================================================================
#  go_backward_any method has been generated for the three-wheeled moving
#  objec to go backward without any limitation of running_time
# =======================================================================

def just_go_backward(speed):

    # set left motor to go backward by GPIO and motor_module
    setup_base.motor(setup_base.backward0, setup_base.Motor_Left_A, setup_base.Motor_Left_B)
    GPIO.output(setup_base.Motor_Left_PWM, GPIO.HIGH)

    # set right motor to go backward by GPIO and motor_module
    setup_base.motor(setup_base.backward1, setup_base.Motor_Right_A, setup_base.Motor_Right_B)
    GPIO.output(setup_base.Motor_Right_PWM, GPIO.HIGH)

    # set left and right Pwm to get speed
    setup_base.Left_Pwm.ChangeDutyCycle(speed)
    setup_base.Right_Pwm.ChangeDutyCycle(speed)

# =======================================================================
#  go_forward_any method has been generated for the three-wheeled moving
#  objec to go forward with the limitation of running_time
# =======================================================================

def go_forward(speed, running_time):

    # set left motor to go forward by GPIO and motor_module
    setup_base.motor(setup_base.forward0, setup_base.Motor_Left_A, setup_base.Motor_Left_B)
    GPIO.output(setup_base.Motor_Left_PWM, GPIO.HIGH)

    # set right motor to go forward by GPIO and motor_module
    setup_base.motor(setup_base.forward1, setup_base.Motor_Right_A, setup_base.Motor_Right_B)
    GPIO.output(setup_base.Motor_Right_PWM, GPIO.HIGH)

    # set left and right Pwm to get speed
    setup_base.Left_Pwm.ChangeDutyCycle(speed)
    setup_base.Right_Pwm.ChangeDutyCycle(speed)

    # stop motor after running_time
    time.sleep(running_time)
    stop()

# =======================================================================
#  go_backward_any method has been generated for the three-wheeled moving
#  objec to go backward with the limitation of running_time
# =======================================================================

def go_backward(speed, running_time):

    # set left motor to go backward by GPIO and motor_module
    setup_base.motor(setup_base.backward0, setup_base.Motor_Left_A, setup_base.Motor_Left_B)
    GPIO.output(setup_base.Motor_Left_PWM, GPIO.HIGH)

    # set right motor to go backward by GPIO and motor_module
    setup_base.motor(setup_base.backward1, setup_base.Motor_Right_A, setup_base.Motor_Right_B)
    GPIO.output(setup_base.Motor_Right_PWM, GPIO.HIGH)

    # set left and right Pwm to get speed
    setup_base.Left_Pwm.ChangeDutyCycle(speed)
    setup_base.Right_Pwm.ChangeDutyCycle(speed)

    # stop motor after running_time
    time.sleep(running_time)
    stop()


# =======================================================================
# define the stop module
# =======================================================================

def stop():
    # the speed of left and right motor will be set as LOW
    GPIO.output(setup_base.Motor_Left_PWM, GPIO.LOW)
    GPIO.output(setup_base.Motor_Right_PWM, GPIO.LOW)
    # left and right motor will be stopped with function of ChangeDutyCycle(0)
    setup_base.Left_Pwm.ChangeDutyCycle(0)
    setup_base.Right_Pwm.ChangeDutyCycle(0)


def pwm_setup():
    # left and right motor pwm will set 0 to be stable
    setup_base.Left_Pwm.start(0)
    setup_base.Right_Pwm.start(0)

# if there is unexpected occurrence
def pwm_low():
    #make motor as LOW and stop
    stop()
    # set GPIO clear
    GPIO.cleanup()