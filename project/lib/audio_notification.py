from machine import Pin, PWM
from time import sleep,time

class Audio_Notification(PWM):
    def __init__(self, pin, debug=False):
        super().__init__(Pin(pin))
        self.__debug = debug
        self.duty_u16(0) 
        self.__last_toggle_time = time()
        
    def beep(self, freq=1000, duration=500):
            self.freq(freq)
            self.duty_u16(37268)
            sleep(duration / 1000)
            self.duty_u16(0)
            if self.__debug:
                print('Beep')
        
    def warning_on(self):
        if self.__debug:
            print('Warning on')
        now = time()
        if now - self.__last_toggle_time >= .5:
            self.beep(freq=500, duration=100)
            self.__last_toggle_time = now
            
    def warning_off(self):
        if self.__debug:
            print('warning off')
        self.duty_u16(0)