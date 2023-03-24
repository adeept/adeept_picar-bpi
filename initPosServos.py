#!/usr/bin/env python3
# File name   : init
# Description : Control Servos
# Author      : William
# Date        : 2019/02/23
# import time
# import Adafruit_PCA9685

# pwm = Adafruit_PCA9685.PCA9685()
# pwm.set_pwm_freq(50)

# while 1:
# 	pwm.set_all_pwm(0, 300)
# 	time.sleep(1)
	
# https://github.com/adafruit/Adafruit_CircuitPython_PCA9685
import time
from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

i2c = busio.I2C(SCL, SDA)
pca = PCA9685(i2c)
pca.frequency = 50
