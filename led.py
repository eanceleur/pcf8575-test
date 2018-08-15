#!/usr/bin/python

import smbus
import time

bus = smbus.SMBus(1)    # 1 = /dev/i2c-1 = i2cdetect first argument

ADDRESS = 0x20      # pcf 8575 address

sleep = 1.0

# read pcf8575 ports values and show them
def print_port():
        val = bus.read_word_data( ADDRESS, 0 )
        print('p7..p0 = {0}, p17..p10 = {1}'.format( bin(val & 0xff ), bin(val >> 8) ))

# init ports values (which is optionnal as there at up level by default)
bus.write_byte_data(ADDRESS, ~ 0x00, ~ 0x00)

# main loop Ctrl-C to break it...
while True:
        # blue on p10
        print('blue')
	bus.write_byte_data(ADDRESS, ~ 0x00, ~ 0x01)
        print_port()
	time.sleep( sleep )
        # red on p2
        print('red')
	bus.write_byte_data(ADDRESS, ~ 0x02, ~ 0x00)
        print_port()
	time.sleep( sleep )
        # green on p5
        print('green')
	bus.write_byte_data(ADDRESS, ~ 0x20, ~ 0x00)
        print_port()
	time.sleep( sleep )

