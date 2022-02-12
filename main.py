#This code runs on Raspberry Pi Pico via MicroPython
import machine
import utime
import random
from machine import PWM, Pin

pinLED1 = 15
pinLED2 = 14

portLED1 = machine.Pin(pinLED1, machine.Pin.OUT)
portLED2 = machine.Pin(pinLED2, machine.Pin.OUT)

pwmLED1 = PWM( portLED1 )
pwmLED2 = PWM( portLED2 )
pwmLED1.freq( 1000 )
pwmLED2.freq( 1000 )

def main():
    value = random.random()
    th = 0.05

    while True:
        if value < 0.5:
            value = value + 2.0 * value ** 2
        else:
            value = value - 2.0 * (1.0 - value) ** 2
        if value <= th or (1 - th) <= value:
           value = random.uniform(0.1, 0.9)
        pwm = int(65535 * value)

        pwmLED1.duty_u16(pwm)
        pwmLED2.duty_u16(65535 - pwm)

        utime.sleep(0.1)

if __name__ == '__main__':
    main()
