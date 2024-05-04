from machine import Pin, PWM
import time
import random
from sensor import HCSR04
import asyncio

led_board = Pin(8, Pin.OUT)  # to turn control the blue LED on the board
led_r = PWM(0, freq=20, duty_u16=65535)  # Full duty cycle for red
led_g = PWM(1, freq=20, duty_u16=65535)  # No duty cycle for green
led_b = PWM(2, freq=20, duty_u16=65535)  # No duty cycle for blue
buzzer = Pin(10, Pin.OUT)  # to control the buzzer


def calculate_intensity(intensity_value):
    return 11 - intensity_value


def red_color(r_value):
    """Set the red color of the RGB led- between 0 to 255"""
    PWM(0, freq=50, duty_u16=abs((r_value*257)-65535))


def green_color(g_value):
    """Set the green color of the RGB led- between 0 to 255"""
    PWM(1, freq=50, duty_u16=abs((g_value*257)-65535))


def blue_color(b_value):
    """Set the blue color of the RGB led- between 0 to 255"""
    PWM(2, freq=50, duty_u16=abs((b_value*257)-65535))


def buzzer_solid_on():
    buzzer.value(1)


def buzzer_solid_off():
    buzzer.value(0)


def buzzer_blink():
    buzzer.value(1)
    time.sleep(0.02)
    buzzer.value(0)
    time.sleep(0.02)


def board_led_blink():
    led_board.value(1)
    time.sleep(0.5)
    led_board.value(0)
    time.sleep(0.5)


def board_led_blink_fast():
    led_board.value(1)
    time.sleep(0.05)
    led_board.value(0)
    time.sleep(0.05)


def borad_led_on():
    led_board.value(0)


def borad_led_off():
    led_board.value(1)


def blue_blink():
    red_color(0)
    green_color(0)
    blue_color(255)
    time.sleep(0.05)
    blue_color(0)
    time.sleep(0.05)


def normal_operation():
    # borad_led_off()
    r_value = random.randint(0, 255)
    g_value = random.randint(0, 255)
    b_value = random.randint(0, 255)
    for i in range(50):
        red_color(int((r_value/calculate_intensity(10)) * i/50))
        green_color(int((g_value/calculate_intensity(10)) * i/50))
        blue_color(int((b_value/calculate_intensity(10)) * i/50))
        time.sleep(0.02)
    for i in range(50):
        red_color(int((r_value/calculate_intensity(10)) * (50-i)/50))
        green_color(int((g_value/calculate_intensity(10)) * (50-i)/50))
        blue_color(int((b_value/calculate_intensity(10)) * (50-i)/50))
        time.sleep(0.02)
    time.sleep(0.5)


def danger_operation():
    borad_led_off()
    red_color(255)
    green_color(0)
    blue_color(0)
    time.sleep(0.1)


def short_dis():
    buzzer_solid_on()
    danger_operation()


def mid_dis():
    board_led_blink_fast()
    blue_blink()
    buzzer_blink()


def long_dis():
    buzzer_solid_off()
    normal_operation()


my_sensor = HCSR04(trigger_pin=3, echo_pin=4)

distance = 199
while True:
    distance = my_sensor.distance_cm()
    intensity = round(255 - distance * (255 / 50))
    intensity = min(255, max(0, intensity))
    blue_color(intensity)
    print(my_sensor.distance_cm())
