#!/bin/bash

# TODO : script to update for release > v2.0

while [ true ]
do

VALUE="0xFD 0xFF"
echo "red ($VALUE)"
i2cset -y 1 0x20  $VALUE

# get status asking a word value
i2cget -y 1 0x20 0 w
sleep 1

VALUE="0xDF 0xFF"
echo "green ($VALUE)"
i2cset -y 1 0x20 $VALUE
i2cget -y 1 0x20 0 w
sleep 1

VALUE="0xFF 0xFE"
echo "blue ($VALUE)"
i2cset -y 1 0x20 $VALUE
i2cget -y 1 0x20 0 w
sleep 1

done


