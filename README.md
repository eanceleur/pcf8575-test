# pcf8575-test
Small tests with Rpi like hardware, i2c bus, pcf 8575 and leds...

# hardware
* orangepi one plus (http://www.orangepi.org/OrangePiOneplus/)
  (its 26 pins port extension is the same as raspberrypi one)
* pcf8575 (i2c port extender 16 ports)
* resistors : 1k, 100k
* leds

pictures :
https://www.instagram.com/p/BmX561CHHG3/?utm_source=ig_web_copy_link

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
Fine, pcf8575 address is 0x20

# set pcf8575 ports

i2cset -y 1 0x20 0x01 0x00
* 1 = i2cbus (same as i2cdetect parameter, on pin 3 and 5)
* 0x20 = pcf i2c address (i2cdetect)
* 0x01 = p0 to p7
* 0x00 = p10 to p17

```
       p7  p6  p5  p4  p3  p2  p1  p0
0x01 =  0   0   0   0   0   0   0   1
       p17 p16 p15 p14 p13 p12 p11 p10
```
Don't forget : as in pcf8575 datasheet, leds are ON with a zero level... meaning that a value of 0x01 switch off led plugged on p0
