#!/bin/bash

# hardware : leds on p1 and p10

while [ true ]
do
# 1 = i2cbus (pin 3 and 5)
# 0x20 = pcf i2c adress (i2cdetect)
# 0x02 = p0 to p7 (p7 p6 p5 p4 p3 p2 p1 p0)
# 0x00 = p10 to p17 (p17 p16 p15 p14 p13 p12 p11 p10)
i2cset -y 1 0x20 0x02 0x00

# get status asking a word value
i2cget -y 1 0x20 0 w
sleep 1
# switch off first ledm switch one second
i2cset -y 1 0x20 0x00 0x01 
sleep 1
i2cget -y 1 0x20 0 w
done

