#!/usr/bin/env python3
import serial
import time

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.flush()


def Serialfn(value):
    ser.write(str(value).encode('ascii'))
    time.sleep(1)
    # if you want it to write in the shell
    # line = ser.readline().decode('utf-8').rstrip()
    # print(line)
