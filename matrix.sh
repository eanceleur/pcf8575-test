#!/bin/bash

i2cset -y 1 0x21 0xFF 0xFF
i2cset -y 1 0x20 0xFF 0xFF

while true
do

  # columns
  for o in 0 1 2 3 4 5 6 7
  do
    mo=`dc -e "2 $o ^ p"`
    i2cset -y 1 0x21 $((0xFF^$mo)) 0xFF

    # colors
    for c in 0 1 2
    do

      # lines
      for l in 0 1 2 3 4 5 6 7
      do
        ml=`dc -e "2 $l ^ p"`
        i2cset -y 1 0x20 $((0xFF^$ml)) $c
        sleep 0.1
      done
    done
  i2cset -y 1 0x20 0xFF 0xFF
  done
done


i2cset -y 1 0x21 0xFF 0xFF

