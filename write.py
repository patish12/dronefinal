# write images to folders

import time

class Writer:
    """Stores drone images to data folders, automatically"""
    
    def __init__(self):
        self.time = time.time()