# -*- coding: utf-8 -*-
import wiringpi
import time
import sys

servo_pin  =  12

# get degree
param = sys.argv
set_degree = int(param[1])
print(set_degree)


wiringpi.wiringPiSetupGpio()
# input / output
wiringpi.pinMode( servo_pin, 2 )


wiringpi.pwmSetMode(0)
wiringpi.pwmSetRange(1024)
wiringpi.pwmSetClock(375)
    
wiringpi.pwmWrite( servo_pin, set_degree )

if ( set_degree >= -90 ):
    move_deg = int( 81 + 41 / 90 * set_degree )
    wiringpi.pwmWrite( servo_pin, move_deg )


