
import cv2
import drone
from defines import *

if __name__ == '__main__':
    # main loop
    if STATE == RunMode.ONLINE:
        d = drone.Drone()
        d.connect_drone()
        while True:
            img = d.get_frame()
            # img = cv2.resize(img, (360, 240))
            cv2.imshow("Image", img)
            cv2.waitKey(1)
            print(d.get_battery())

