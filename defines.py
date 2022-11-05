# general defines

from Enum import enum

class RunMode(Enum):
    ONLINE = 0
    OFFLINE = 1
    CREATE_VIDEO = 2

STATE = RunMode.CREATE_VIDEO