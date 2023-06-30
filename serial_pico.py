import serial

ser = serial.Serial('/dev/ttyACM0', 115200)  # Open the serial connection

duty_cycle = 75  # The duty cycle value (0-100)
data_to_send = str(duty_cycle)  # Convert the duty cycle to a string
ser.write(data_to_send.encode())  # Send the data over the serial connection

ser.close()  # Close the serial connection

