from abc import ABC, abstractmethod

class Switchtable(ABC):
    @abstractmethod
    def turn_on(self):
        """Turn on the device"""

    @abstractmethod
    def turn_off(self):
        """Turn off the device"""

class LightBulb(Switchtable):
    def turn_on(self):
        print("LightBulb: turned on...")
    
    def turn_off(self):
        print("LightBulb: turned off...")

class Piano(Switchtable):
    def turn_on(self):
        print("Piano: turned on...")
    
    def turn_off(self):
        print("Piano: turned off...")   

class PC(Switchtable):
    def turn_on(self):
        print("PC: turned on...")
    
    def turn_off(self):
        print("PC: turned off...")   

class ElectricPowerSwitch():

    def __init__(self, dev:Switchtable):
        self.device = dev
        self.on = False

    def press(self):
        if self.on:
            self.device.turn_off()
            self.on = False
        else:
            self.device.turn_on()
            self.on = True

lightbulb = LightBulb()
piano     = Piano()
pc        = PC()

switch = ElectricPowerSwitch(piano)
switch.press()
switch.press()
