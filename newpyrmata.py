import pyfirmata
import time

port = input("Enter port number only (e.g. 3 for COM3): ")
com = "COM" + port
print(f"Connecting to {com}...")

# Connect to the Arduino board
board = pyfirmata.Arduino(com)

# Start an iterator thread so serial buffer doesn't overflow
it = pyfirmata.util.Iterator(board)
it.start()

# Set pin 13 as output
led_pin = board.digital[12]
led_pin.mode = pyfirmata.OUTPUT

# Blink LED
while True:
    led_pin.write(1)
    print("LED ON - hello")
    time.sleep(1)

    led_pin.write(0)
    print("LED OFF - hii")
    time.sleep(1)