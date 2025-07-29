import serial
import time

# Open serial port
ser = serial.Serial('COM10', 9600, timeout=1)  # Windows: COM3, Linux: /dev/ttyUSB0
time.sleep(2)  # Wait for connection

# Send data
ser.write(b'G0 X200\n')

# Read response
response = ser.readline().decode('utf-8').strip()
print("Received:", response)

ser.close()
