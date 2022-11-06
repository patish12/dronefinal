import pygame
from defines import DEBUG, DATA_DIR

class Keyboard:
    "Handles keyboard pressing"

    def __init__(self):
        self.me = pygame.init()
        self.open_window()

    def _print(self, *s):
            if DEBUG:
                print('keyboard:', *s)

    def open_window(self):
        self.me.display.set_mode((400,400))
    
    def get_key(self, keyName):
        pressed = False
    
    