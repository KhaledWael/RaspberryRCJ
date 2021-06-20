from serial_communication import *
import time

while True:
    x = "test Data from fn\n"
    Serialfn(x)
    # line = ser.readline().decode('utf-8').rstrip()
    # print(line)
    time.sleep(1)
