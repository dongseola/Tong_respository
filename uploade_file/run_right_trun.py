#########################################################################
# 20171618 Dong_Seola 's code
# 2017. 10. 30
# this star_run.py file is Executable code
#########################################################################

# =======================================================================
# import GPIO library and time module
# =======================================================================
import RPi.GPIO as GPIO
import time

# =======================================================================
# set up GPIO mode as BOARD
# set GPIO warnings as flase
# =======================================================================

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

# =======================================================================
# import get_Distance() method in the ultrasonic_sensor_module
# =======================================================================
import ultrasonic_sensor_module

# get_Distance()

# =======================================================================
# import turn_module
# =======================================================================
import turn_module

# left_motor(x)   #right_motor(x)  - set right and left motor to move
# right_SwingTurn(speed, runningtime) - rihgt wheel is stop
# left_SwingTurn(speed, runningtime) - left wheel is stop
# right_PointTurn(speed, runningtime) - right wheel go back
# left_PointTurn(speed, runningtime) - left wheel go back

# =======================================================================
# import just_go_forward(), just_go_backward(),
# stop(), pwm_setup(), and pwm_low() methods in the module of go_module
# =======================================================================
import go_module

# motor(x, Motor_A, Motor_B) - set right or left motor to move
# just_go_forward(speed) - go forward while other stimulation get
# go_backward_any(speed) - go backward while other stimulation get
# go_forward(speed, running_time) - go forward while running time
# go_backward(speed, running_time) - go backward while running time

# pwm_setup() - get pwm 0 both wheel
# pwm_low() - if there is unexpected occurrence
# stop() - get pwm to stop

# =======================================================================
# setup and initilaize the left motor and right motor
# =======================================================================

go_module.pwm_setup()

# =======================================================================
#  define your variables and find out each value of variables
#  eg) dis and obstacle
# =======================================================================

dis = 17  #20
obstacle = 0  # how many times does the car meet

# Swing Turn 's angle
SwingPr1 = 50
SwingTr1 = 0.4
# Point Turn 's angle
SwingPr2 = 30
SwingTr2 = 0.4
# The speed that the executor wants
speed = 43

# ========================================================================
#  to perform the start_run with import
#  eg) go for,back ward and trun swing,point
# ========================================================================

try:
    while True:
        # ultra sensor replies the distance back
        distance = ultrasonic_sensor_module.get_Distance()
        print('distance= ', distance)

        # when the distance is above the dis, moving object forwards
        if (distance > dis):
            if obstacle ==0 or 1:
                go_module.just_go_forward(speed)
                print('obstacle=', obstacle)
            else :
                go_module.go_forward(speed,3)

        # when the distance is below the dis
        else:
            # stop and wait 1 second
            go_module.stop()
            time.sleep(1)
            #Swing right turn
            if obstacle==0:
                turn_module.right_SwingTurn(SwingPr1,SwingTr1)
                time.sleep(1)
                obstacle +=1
            #Poin right trun
            elif obstacle==1:
                turn_module.right_PointTurn(SwingPr2,SwingTr2)
                time.sleep(1)
                obstacle +=1
		


# when the Ctrl+C key has been pressed,
# the moving object will be stopped
except KeyboardInterrupt:
    go_module.pwm_low()
