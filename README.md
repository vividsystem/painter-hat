# painter-hat
A stepper motor hat that sucks less.

Disclaimer: I haven't gotten the possibility to actually manufacture this yet. Therefore it might not work

Features:
    - dual stepper-motor driver control
    - support for A4988, TMC2208, TMC2209, etc. driver modules 
    - hot-swap replacement for [Waveshare Stepper Motor HAT](https://www.waveshare.com/wiki/Stepper_Motor_HAT)*

*one caveat: you are now forced to use software microstepping controls as different drivers have different options

## Motivaiton
I was very frustrated working with the [Waveshare Stepper Motor HAT](https://www.waveshare.com/wiki/Stepper_Motor_HAT).
The quality control seems to be off as two HATs I ordered didn't work. 
Their documentation is good and the provided codes works but there are some minor issues that led me to write my own code to
control the hat. Most importantly you can't swap drivers (in case you fry them for example) which led me to buy multiple
new drivers after testing and subsequently frying the drivers. This sucks because for my use case I have to get a whole
new HAT even when one of the two drivers is still working.

## Hardware
- supports up to 100W (20V@5A)


