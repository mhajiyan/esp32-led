from pymata4 import pymata4
import numpy as np
import time

board = pymata4.Pymata4()

board.set_pin_mode_pwm_output(8)
board.set_pin_mode_pwm_output(9)
board.set_pin_mode_pwm_output(10)

time.sleep(1)
board.pwm_write(8, 0)
board.pwm_write(9, 255)
board.pwm_write(10, 255)
