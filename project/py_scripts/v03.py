from machine import Pin
from time import sleep, time


class Led_Light(Pin):
    def __init__(self, pin, flashing=False, debug=False):
        super().__init__(pin, Pin.OUT)
        self.led_light_state
        self.__debug = debug
        self.__pin = pin
        self.__flashing = flashing

    def on(self):
        self.high()
        if self.__debug:
            print(f'LED connected to Pin {self.__pin} is {self.led_light_state}')
            
    def off(self):
        self.low()
        if self.__debug:
            print(f'LED connected to Pin {self.__pin} is {self.led_light_state}')

    def toggle(self):
        if self.value() = 0:
            self.on()
        elif self.value() = 1:
            self.off()

    @property
    def led_light_state(self):
        return self.value()
    
    @led_light_state.setter
    def led_light_state(self, value):
        if value == 0:
            self.off()
        elif value == 1:
            self.on()

red_light = Led_Light(3, False, True)

while True:
    print(red_light.led.light_state)
    red_light.led_light_state = 1
    sleep(0.25)
    print(red_light.led_light_state)
    red_light.led_light_state = 0
    sleep(0.25)
