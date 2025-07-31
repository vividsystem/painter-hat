import RPi.GPIO as GPIO
import time

class BaseDriver():
    def __init__(self, dir_pin, step_pin, enable_pin, mode_pins):
        self.dir_pin = dir_pin
        self.step_pin = step_pin        
        self.enable_pin = enable_pin
        self.mode_pins = mode_pins
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.dir_pin, GPIO.OUT)
        GPIO.setup(self.step_pin, GPIO.OUT)
        GPIO.setup(self.enable_pin, GPIO.OUT)
        GPIO.setup(self.mode_pins, GPIO.OUT)
        
    def Stop(self):
        GPIO.output(self.enable_pin, 0)
    

        
    def TurnStep(self, steps, forward = True, stepdelay=0.005):
            
        GPIO.output(self.enable_pin, 1)
        GPIO.output(self.dir_pin, 0 if forward else 1)
        if (steps == 0):
            return
            
        for i in range(steps):
            GPIO.output(self.step_pin, True)
            time.sleep(stepdelay)
            GPIO.output(self.step_pin, False)
            time.sleep(stepdelay)
