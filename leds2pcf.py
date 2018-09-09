
import smbus
from multiprocessing import Process, Queue


class Leds :

  # a row = a led
  mapping_rows = ( 0x4000, 0x8000 )
  # R G B
  mapping_colors = ( 0x0100, 0x0200, 0x0400 )
  # column
  mapping_cols = ( 0x0001, 0x0002, 0x0004, 0x0008 )
  
  # init smbus
  def __init__(self, i2cbus, pcf_address ):
    self.i2cbus = i2cbus
    self.pcf_address = pcf_address
    self.debug = False
    self.bus = smbus.SMBus( self.i2cbus )

  def set_debug( self, debug ):
    if debug == True:
	  self.debug = True
    else:
	  self.debug = False
	  
  # write data to pcf
  def write2pcf( self, ports ):
    p0p7 = ports & 0x00ff
    p10p17 = ports >> 8
	# depending on hardware, we need to inverse data as leds swith on on zero level
    p0p7 = ~ p0p7
    p10p17 = p10p17 ^ 0xF0    # colors are not inversed
    self.bus.write_byte_data(self.pcf_address, p0p7 , p10p17 )
    if self.debug:
      print( "  i2c write data : 0x{0:X} 0x{1:X} 0x{2:X}".format( self.pcf_address, p0p7 & 0xFF, p10p17 & 0xFF ))

  def turn_on( self, row, col, color ):
    
    ports = self.mapping_rows[ row ]

    if color == 'R':
      ports |= self.mapping_colors[0]
    elif color == 'G':
      ports |= self.mapping_colors[1]
    elif color == 'B':
      ports |= self.mapping_colors[2]
    else:
      pass

    ports |= self.mapping_cols[col]
	
    if self.debug:
      print( "ports = {0}".format( hex(ports)))
    
    self.write2pcf( ports )

  def turn_off(self):
    if self.debug:
      print( "turn off" )
    self.write2pcf( 0 )


class LedsMatrix( Leds ):

  def __init__(self, i2cbus, pcf_address ):
    Leds.__init__( self, i2cbus, pcf_address )

    # init matrix
    self.leds_matrix = []
    for i in range(2):
      self.leds_matrix.append([])
      for j in range(4):
        self.leds_matrix[i].append('O') 

    self.queue = Queue()
    self.io_thread = Process(target=self.internal_loop, args=(self.queue,self.leds_matrix))
    self.io_thread.start()

  def internal_loop(self, queue, matrix ):
    print("internal loop started")
    while True:
      try:
        (row,col,color) = queue.get_nowait()
        matrix[row][col] = color
      except:
        pass
      for row in range(len(matrix)):
        for col in range(len(matrix[row])):
          self.turn_on( row, col, matrix[row][col] )

  def print_matrix(self):
    print( self.leds_matrix[:] )

  def update(self, row, col, color):
    self.queue.put( (row,col,color) )
