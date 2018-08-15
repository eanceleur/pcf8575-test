# pcf8575-test
Small tests with Rpi like hardware, i2c bus, pcf 8575 and leds...

Just to make leds blinking for hardware and sofware tryouts....


# hardware
* orangepi one plus (http://www.orangepi.org/OrangePiOneplus/)
  (its 26 pins port extension is the same as raspberrypi one)
* pcf8575 (i2c port extender 16 ports)
* resistors : 1k, 100k
* leds

# releases
* v1.0 : https://github.com/eanceleur/pcf8575-test/wiki/Release-v1.0
* v1.1 : https://github.com/eanceleur/pcf8575-test/wiki/Release-v1.1


# find pcf 8575 address
```
root@OrangePiH6:~# i2cdetect -y 0
Error: Could not open file `/dev/i2c-0' or `/dev/i2c/0': No such file or directory
```
It means there's no i2c bus at number 0, try again :
```
root@OrangePiH6:~# i2cdetect -y 1
     0  1  2  3  4  5  6  7  8  9  a  b  c  d  e  f
00:          -- -- -- -- -- -- -- -- -- -- -- -- --
10: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
20: 20 -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
30: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
40: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
50: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
60: -- -- -- -- -- -- -- -- -- -- -- -- -- -- -- --
70: -- -- -- -- -- -- -- --
```
Fine, pcf8575 address is 0x20 and we use i2c bus number 1


