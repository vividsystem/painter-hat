# painter-hat
A stepper motor hat that sucks less.

Disclaimer: I haven't gotten the possibility to actually manufacture this yet. Therefore it might not work

Features:
    - dual stepper-motor driver control
    - 100W USB-C PD to power motors and raspberry pi
    - support for A4988, TMC2208, TMC2209, etc. driver modules including UART control
    - meant as replacement for [Waveshare Stepper Motor HAT](https://www.waveshare.com/wiki/Stepper_Motor_HAT)*

*not completely hot-swap. you will have to use a different firmware

## Motivaiton
I was very frustrated working with the [Waveshare Stepper Motor HAT](https://www.waveshare.com/wiki/Stepper_Motor_HAT).
The quality control seems to be off as two HATs I ordered didn't work. 
Their documentation is good and the provided codes works but there are some minor issues that led me to write my own code to
control the hat. Most importantly you can't swap drivers (in case you fry them for example) which led me to buy multiple
new drivers after testing and subsequently frying the drivers. This sucks because for my use case I have to get a whole
new HAT even when one of the two drivers is still working.


## Firmware
Currently outdated!
