#Main program 

from win32api import *
from win32gui import *
import win32con
import sys, os
import struct
import time
import simplejson as json
import notification as note
import DataInterface as data
import DateWatch as date


if __name__ == '__main__':
    while True:
        time.sleep(1)
        #date.CheckForEvent(data.LoadFile("./data.json"))
        print(data.LoadFile("./data.json")[3])