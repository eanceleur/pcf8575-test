#!/bin/bash

# hardware : leds on p1 and p10

while [ true ]
do
# first led is p10 
i2cset -y 1 0x20 0x02 0x00

# get status asking a word value
i2cget -y 1 0x20 0 w
sleep 1

# switch off first led switch one second
i2cset -y 1 0x20 0x00 0x01 
i2cget -y 1 0x20 0 w
sleep 1

done

