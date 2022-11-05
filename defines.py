# general defines

from enum import Enum

class RunMode(Enum):
    ONLINE = 0
    OFFLINE = 1
    CREATE_VIDEO = 2

STATE = RunMode.CREATE_VIDEO
DEBUG = True
DATA_DIR = 'data'