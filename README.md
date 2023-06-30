# Raspberry Pi Pico PWM Control via USB/UART

This project demonstrates how to control the duty cycle of a PWM signal on a Raspberry Pi Pico using USB/UART communication. The code provided allows you to send a duty cycle value from your laptop to the Raspberry Pi Pico, which then adjusts the PWM signal accordingly.

## Prerequisites

- Raspberry Pi Pico board
- Laptop or computer with a USB port
- Python and `serial` module installed on your laptop

## Hardware Setup

1. Connect the Raspberry Pi Pico to your laptop using a USB cable.
2. Connect an LED or any other suitable component to GPIO Pin 25 (PWM output pin).

## Software Setup

1. write the code in the `main.py` file to your Raspberry Pi Pico using your preferred method (Thonny).
2. On your laptop, ensure that the `serial` module is installed. You can install it using the following command:
   
$pip install pyserial

 
## Usage

1. Open the `main.py` file on your Raspberry Pi Pico in a MicroPython editor and save it to the board.
2. Run the `serial_pico.py` file on your laptop using Python:

$python serial_pico.py

3. The laptop will send the duty cycle value over the USB/UART connection to the Raspberry Pi Pico, which will adjust the PWM signal accordingly.
4. Observe the connected LED or component to see the PWM control in action.

## Troubleshooting

- Make sure the Raspberry Pi Pico is properly connected to your laptop via USB.
- Check that the correct serial port is specified in the `serial_pico.py` file (e.g., `'/dev/ttyUSB0'` on Linux or `'COM3'` on Windows).

