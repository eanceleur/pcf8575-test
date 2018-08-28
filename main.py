#!/usr/bin/python

import time

import leds2pcf

# create object with i2cbus number and pcf address
leds = leds2pcf.Leds( 1, 0x20 )
leds.set_debug(True)

# show each color on each leds
def the_loop():
  while True:
    for row in range(2):
      for col in range(4):
        for color in ['R','G','B']:
          leds.turn_on( row, col, color )
          time.sleep(1)

# show one matrix pattern during 'duration' parameter
def matrix_one( matrix, duration=float("inf") ):
  stop = False
  t_begin = time.time()
  while not stop:
    for row in range(len(matrix)):
      for col in range(len(matrix[row])):
        leds.turn_on( row, col, matrix[row][col] )
    stop = ( time.time() - t_begin ) >= duration

# define different patterns
def matrix_several():
  m = [
# first combination
    { "duration": 5,
      "matrix": [
        ['R', 'B', 'R', 'G' ],
        ['G', 'R', 'B', 'R' ]
      ] },
    { "duration": 5,
      "matrix": [
        ['G', 'R', 'B', 'R' ],
        ['R', 'B', 'R', 'G' ],
      ] },
# second display
    { "duration": 2,
      "matrix": [
        ['G', 'G', 'G', 'G' ],
        ['B', 'B', 'B', 'B' ],
      ] },
    { "duration": 2,
      "matrix": [
        ['B', 'G', 'G', 'G' ],
        ['B', 'B', 'B', 'G' ],
      ] },
    { "duration": 2,
      "matrix": [
        ['B', 'B', 'G', 'G' ],
        ['B', 'B', 'G', 'G' ],
      ] },
    { "duration": 2,
      "matrix": [
        ['B', 'B', 'B', 'G' ],
        ['B', 'G', 'G', 'G' ],
      ] },
    { "duration": 2,
      "matrix": [
        ['B', 'B', 'B', 'B' ],
        ['G', 'G', 'G', 'G' ],
      ] },
  ]
  for i in range(len(m)):
    matrix_one( m[i]["matrix"], m[i]["duration"] )

# main menu
print('Choose : \n')
print(' 1 - loop rows, columns, colors\n')
print(' 2 - matrix\n')

f = input()
f = int(f)
if f == 1:
  the_loop()
elif f == 2:
  leds.set_debug(False)
  while True:
    matrix_several( )

leds.turn_off()

