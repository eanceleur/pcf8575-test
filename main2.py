#!/usr/bin/python

import time

import leds2pcf

# create object with i2cbus number and pcf address
leds = leds2pcf.LedsMatrix( 1 )
leds.set_debug(True)

leds.print_matrix()

while True:
  for c in ( 'R', 'B', 'G' ):
    for i in range(8):
      for j in range(8):
        leds.update(i,j,c)
        time.sleep(0.5)

