
import smbus
from multiprocessing import Process, Queue


class Leds :

  # R G B
  mapping_colors = ( 0x0000, 0x0001, 0x0002 )
  
  # init smbus
  def __init__(self, i2cbus ):
    self.i2cbus = i2cbus
    self.pcf_address0 = 0x20
    self.pcf_address1 = 0x21
    self.debug = False
    self.bus = smbus.SMBus( self.i2cbus )
    self.color = 0xffff

  def set_debug( self, debug ):
    if debug == True:
	  self.debug = True
    else:
	  self.debug = False
	  
  # write data to pcf
  def write2pcf_rowcol( self, ports ):
    p0p7 = ~ (ports & 0x00ff)
    p10p17 = ~ (ports >> 8)
    self.bus.write_byte_data(self.pcf_address0, p0p7 , p10p17 )
    if self.debug:
      print( "  i2c write data : 0x{0:X} 0x{1:X} 0x{2:X}".format( self.pcf_address0, p0p7 & 0xFF, p10p17 & 0xFF ))

  def write2pcf_color( self, ports ):
    p0p7 = ports & 0x00ff
    p10p17 = ports >> 8
    self.bus.write_byte_data(self.pcf_address1, p0p7 , p10p17 )
    if self.debug:
      print( "  i2c write data : 0x{0:X} 0x{1:X} 0x{2:X}".format( self.pcf_address1, p0p7 & 0xFF, p10p17 & 0xFF ))

  def map_color( self, color ):
    if color == 'R':
      return self.mapping_colors[0]
    elif color == 'G':
      return self.mapping_colors[1]
    elif color == 'B':
      return self.mapping_colors[2]
    else:
      return -1
	  
  def turn_on( self, row, col, color ):
    
    ports1 = self.map_color( color )
    if ports1 == -1 :
      return

    ports0 = ((1 << col) << 8) | (1 << row)

    if self.debug:
      print( "ports = {0} {1}".format( hex(ports0), hex(ports1) ) )
    
    if ports1 != self.color :
      self.write2pcf_color( 0xffff )

    self.write2pcf_rowcol( ports0 )
    self.write2pcf_color( ports1 )
    self.color = ports1

  def turn_off(self):
    if self.debug:
      print( "turn off" )
    self.write2pcf_rowcol( 0 )
    self.write2pcf_color( 0 )


class LedsMatrix( Leds ):

  def __init__(self, i2cbus ):
    Leds.__init__( self, i2cbus )

    # init matrix
    self.leds_matrix = []
    self.leds_matrix_size = 8
    for i in range(self.leds_matrix_size):
      self.leds_matrix.append([])
      for j in range(self.leds_matrix_size):
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
      for row in range(self.leds_matrix_size):
        for col in range(self.leds_matrix_size):
          self.turn_on( row, col, matrix[row][col] )

  def print_matrix(self):
    print( self.leds_matrix[:] )

  def update(self, row, col, color):
    self.queue.put( (row,col,color) )
