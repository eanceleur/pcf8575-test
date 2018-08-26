#!/usr/bin/python

import time

import leds2pcf

# create object with i2cbus number and pcf adress
leds = leds2pcf.Leds( 1, 0x20 )
leds.set_debug(True)

def the_loop():
  while True:
    for row in range(2):
      for col in range(2):
        for color in ['R','G','B']:
          leds.turn_on( row, col, color )
          time.sleep(2)

def matrix():
  matrix = [
    [ 'R', 'B' ],
    [ 'B', 'G' ],
  ]
  leds.set_debug(False)
  while True:
    for row in range(len(matrix)):
      for col in range(len(matrix[row])):
        leds.turn_on( row, col, matrix[row][col] )


print('Choose : \n')
print(' 1 - loop rows, columns, colors\n')
print(' 2 - matrix\n')

f = input()
f = int(f)
if f == 1:
  the_loop()
elif f == 2:
  matrix()

leds.turn_off()

