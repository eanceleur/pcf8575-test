#!/usr/bin/python

import time

import leds2pcf

# create object with i2cbus number and pcf adress
leds = leds2pcf.Leds( 1, 0x20 )


for row in range(2):
	for color in ['R','G','B']:
		leds.turn_on( row, color )
		time.sleep(2)

leds.turn_off()

