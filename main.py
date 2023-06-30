from machine import Pin, PWM
from time import sleep
from sys import stdin, exit


pwm_pin = machine.Pin(25)
pwm = machine.PWM(pwm_pin)
print("connection")

while True:
     if input_character = stdin.read(1):
        self
        select_result = uselect.select([stdin], [], [], 0)
        print(input_character)
        
        try:
            value = (input_character stdin.read(1))
            duty_cycle = value if value >= 0 and value <= 100 else 0  # Limit the value to the valid range (0-100)
            pwm.duty_u16(int(duty_cycle * 655.35))  # Set the duty cycle of the PWM signal
        except ValueError:
            pass  # Ignore invalid data

pwm.deinit()
