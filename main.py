import machine
import time

uart = machine.UART(0, baudrate=115200, tx=0, rx=1)  # Use UART 0 with a baud rate of 115200
uart.init(baudrate=115200, bits=8, parity=None, stop=1, tx=0, rx=1)  # Initialize the UART

led_pin = machine.Pin(25, machine.Pin.OUT)  # Pin 25 for controlling the LED
pwm = machine.PWM(led_pin)  # Create a PWM object

while True:
    if uart.any():
        received_data = uart.read(uart.any())  # Read all available data from the UART
        data_string = received_data.decode().strip()  # Convert bytes to string and remove leading/trailing whitespace

        try:
            duty_cycle = int(data_string)  # Convert the received string to an integer
            if duty_cycle >= 0 and duty_cycle <= 100:  # Make sure the value is within the valid range
                pwm.duty_u16(int(duty_cycle * 655.35))  # Scale the duty cycle to 16-bit value (0-65535)
                print("PWM duty cycle set to:", duty_cycle, "%")
            else:
                print("Invalid duty cycle value:", duty_cycle)
        except ValueError:
            print("Invalid data received")

    time.sleep(0.1)  # Delay to avoid flooding the UART
