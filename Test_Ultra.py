from Ultrasonic import *

old_distance = -1
while True:
    dst = int(getDistance())
    if old_distance != dst:
        old_distance = dst
        print(int(dst))
