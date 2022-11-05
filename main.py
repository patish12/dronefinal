
import cv2
import drone
import write
from defines import *

if __name__ == '__main__':
    # main loop
    d = drone.Drone()
    
    if STATE == RunMode.ONLINE:
        d.connect()
        while True:
            print('Press "q" to quit')
            img = d.get_frame()
            # img = cv2.resize(img, (360, 240))
            cv2.imshow(WINDOW_NAME, img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            print(d.get_battery())
            
    elif STATE == RunMode.CREATE_VIDEO:
        w = write.Writer()
        d.connect()
        d.take_off()
        for i in range(100):
            print(f'Recording image {i}')
            img = d.get_frame()
            w.add_image(img)
        d.land()

    else:
        print(f'Support for mode {STATE} not yet implemented')

