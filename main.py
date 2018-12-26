#!/usr/bin/python

import time

import leds2pcf

# create object with i2cbus number
leds = leds2pcf.Leds( 1 )
leds.set_debug(True)

# show each color on each leds
def the_loop():
  while True:
    for row in range(8):
      for col in range(8):
        for color in ['R','G','B']:
          leds.turn_on( row, col, color )
          time.sleep(0.1)

# show each color on all leds
def the_loop_RGB():
  while True:
    for color in ['R','G','B']:
      for row in range(2):
        for col in range(4):
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
    { "duration": 5,
      "matrix": [
        ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R' ],
        ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G' ],
        ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B' ],
        ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R' ],
        ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G' ],
        ['B', 'B', 'B', 'B', 'B', 'B', 'B', 'B' ],
        ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R' ],
        ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'G' ]
      ] },
    { "duration": 5,
      "matrix": [
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O' ],
        ['O', 'O', 'B', 'O', 'O', 'B', 'O', 'O' ],
        ['O', 'O', 'B', 'O', 'O', 'B', 'O', 'O' ],
        ['O', 'O', 'B', 'O', 'O', 'B', 'O', 'O' ],
        ['O', 'O', 'B', 'B', 'B', 'B', 'O', 'O' ],
        ['O', 'O', 'B', 'O', 'O', 'B', 'O', 'O' ],
        ['O', 'O', 'B', 'O', 'O', 'B', 'O', 'O' ],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O' ],
      ] },
    { "duration": 5,
      "matrix": [
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O' ],
        ['O', 'O', 'O', 'G', 'G', 'O', 'O', 'O' ],
        ['O', 'O', 'R', 'O', 'O', 'R', 'O', 'O' ],
        ['O', 'G', 'O', 'O', 'O', 'O', 'G', 'O' ],
        ['O', 'G', 'G', 'G', 'G', 'G', 'G', 'O' ],
        ['O', 'G', 'O', 'O', 'O', 'O', 'G', 'O' ],
        ['O', 'G', 'O', 'O', 'O', 'O', 'G', 'O' ],
        ['O', 'O', 'O', 'O', 'O', 'O', 'O', 'O' ],
      ] },
  ]
  for i in range(len(m)):
    matrix_one( m[i]["matrix"], m[i]["duration"] )

# main menu
print('Choose : \n')
print(' 1 - loop rows, columns, colors\n')
print(' 2 - loop colors, rows, columns\n')
print(' 3 - matrix samples\n')

f = input()
f = int(f)
if f == 1:
  the_loop()
elif f == 2:
  the_loop_RGB()
elif f == 3:
  leds.set_debug(False)
  while True:
    matrix_several( )

leds.turn_off()

