#!/usr/bin/python

import time

import leds2pcf

# create object with i2cbus number and pcf address
leds = leds2pcf.LedsMatrix( 1, 0x20 )
leds.set_debug(True)

leds.print_matrix()

while True:
  for c in ( 'R', 'B', 'G' ):
    for i in range(2):
      for j in range(4):
        leds.update(i,j,c)
        time.sleep(1)

