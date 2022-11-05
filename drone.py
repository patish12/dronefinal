# drone control module

from djitellopy import tello
from defines import DEBUG

class Drone:
    
    def __init__(self):
        """constructor"""
        self.me = tello.Tello()
        self.connected = False
        
    def _print(self, *s):
        if DEBUG:
            print('drone:', *s)
    
    def connect(self):
        """connect to the drone"""
        # todo: can we get the result of connect() and store it in self.connected
        self.me.connect()
        self.me.streamon()
        self._print('connected')

    def disconnect(Self):
        """disconnect the drone"""
        pass
    
    def get_battery(self):
        """returns battery status"""
        return self.me.get_battery()
    
    def land(self):
        """lands the drone"""
        pass
    
    def is_connected(self):
        return self.connected
    
    def get_frame(self):
        """"get next frame"""
        return self.me.get_frame_read().frame

if __name__ == '__main__':
    d = Drone()
    d.connect()