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
      for row in range(8):
        for col in range(8):
          leds.turn_on( row, col, color )
          time.sleep(0.2)

# show one matrix pattern during 'duration' parameter
def matrix_one( matrix, duration=float("inf") ):
  stop = False
  t_begin = time.time()
  while not stop:
    for row in range(len(matrix)):
      for col in range(len(matrix[row])):
        leds.turn_on( row, col, matrix[row][col] )
    stop = ( time.time() - t_begin ) >= duration

def matrix_onev2( matrix, duration=float("inf") ):
  stop = False
  t_begin = time.time()
  while not stop:
    for row in range(len(matrix)):
      col = 0
      for color in str(matrix[row]):
        leds.turn_on( row, col, color )
        col += 1
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

def heart():
  m = [ 
    [
        '........' ,
        '........' ,
        '........' ,
        '........' ,
        '...R....' ,
        '........' ,
        '........' ,
        '........' ,
    ],
    [
        '........' ,
        '........' ,
        '........' ,
        '........' ,
        '..R.R...' ,
        '...R....' ,
        '........' ,
        '........' ,
    ],
    [
        '........' ,
        '........' ,
        '..R.R...' ,
        '.R.R.R..' ,
        '.R...R..' ,
        '..R.R...' ,
        '...R....' ,
        '........' ,
    ],    
    [
        '........' ,
        '........' ,
        '.RR.RR..' ,
        'R..R..R.' ,
        '.R...R..' ,
        '..R.R...' ,
        '...R....' ,
        '........' ,
    ],    
    [
        '........' ,
        '.RR.RR..' ,
        'R..R..R.' ,
        'R.....R.' ,
        '.R...R..' ,
        '..R.R...' ,
        '...R....' ,
        '........' ,
    ],
  ]
  for i in range(len(m)):
    matrix_onev2( m[i], 1 )
  for j in range(5):
    for i in range(4,2, -1):
      matrix_onev2( m[i], 0.5 )
    #matrix_onev2( m[3], 0.5 )
  
def heart_arrow(): 
  arrow = [
    ['........',
     '.RR.RR..',
     'R..R..R.',
     'R.....R.',
     '.R...R..',
     '..R.R...',
     '...R....',
     'B.......'],
    ['........',
     '.RR.RR..',
     'R..R..R.',
     'R.....R.',
     '.R...R..',
     '..R.R...',
     'BB.R....',
     'BB......'],
    ['........',
     '.RR.RR..',
     'R..R..R.',
     'R.....R.',
     '.R...R..',
     '.BB.R...',
     '.BBR....',
     'B.......'],
    ['........',
     '.RR.RR..',
     'R..R..R.',
     'R.....R.',
     '.RBB.R..',
     '..BBR...',
     '.B.R....',
     'B.......'],
    ['........',
     '.RR.RR..',
     'R..R..R.',
     'R.....R.',
     '.R.B.R..',
     '..B.R...',
     '.B.R....',
     'B.......'],
    ['........',
     '.RR.RBB.',
     'R..R..B.',
     'R.....R.',
     '.R.B.R..',
     '..B.R...',
     '.B.R....',
     'B.......'],
    ['......BB',
     '.RR.RRBB',
     'R..R..R.',
     'R.....R.',
     '.R.B.R..',
     '..B.R...',
     '.B.R....',
     '........'],
  ]
  for i in range(len(arrow)):
    matrix_onev2( arrow[i], 0.5 )
  matrix_onev2( arrow[6], 2 )
  
	

# main menu
print('Choose : \n')
print(' 1 - loop rows, columns, colors\n')
print(' 2 - loop colors, rows, columns\n')
print(' 3 - matrix samples\n')
print(' 4 - heart\n')
print(' 5 - heart + arrow\n')

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
elif f == 4:
  leds.set_debug(False)
  while True:
    heart()
elif f == 5:
  leds.set_debug(False)
  while True:
    heart_arrow()

leds.turn_off()

