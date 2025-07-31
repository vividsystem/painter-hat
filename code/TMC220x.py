import RPi.GPIO as GPIO
from BaseDriver import BaseDriver


class TMC220x(BaseDriver):
    def fullstep(self):
        GPIO.output(self.mode_pins, [0,0])
    def halfstep(self):
        GPIO.output(self.mode_pins, [1,0])
    def quarterstep(self):
        GPIO.output(self.mode_pins, [0,1])
    def eighth_step(self):
        GPIO.output(self.mode_pins, [1,1])

    # rest needs uart
