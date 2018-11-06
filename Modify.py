
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

event_list = []

#prints strigns to screen starting from index 0s
def EventListViewer():
    if len(event_list) > 0:
        for index, event in enumerate(event_list):
            print("("+str(index)+"):" + str(event))

def AddEvent():
    print("event day")
    date = input()
    print("event time")
    time = input()
    print("event message")
    message = input()

    event = [date,time,message]
    event_list.append(event)
    print(event_list)

def RemoveEvent():
    if len(event_list) > 0:

        EventListViewer()
        print("enter index of event to remove")
        index = int(input())

        if not (index > len(event_list) - 1):
            del event_list[index]
        else:
            print("Index choice out of bounds")

    else:
        print("There are no events to delete")

#TODO: Add file path verifier
def SelectFile():
    print("Enter file path to valid json event list")
    file_path = input()
    return data.LoadFile(file_path)

def ModifiyEvents():
    modifying = True
    while modifying:
        print("(C)heck scheduled events")
        print("(A)dd new event")
        print("(D)elete scheduled event")
        print("(S)ave scheduled events")
        print("(L)oad a scheduled events file")
        print("(E)xit")
        choice = input().lower()
        if choice == "c":
            EventListViewer()
        elif choice == "a":
            AddEvent()
        elif choice == "d":
            RemoveEvent()
        elif choice =="s":
            data.SaveFile(event_list)
        elif choice == "l":
            imported_json = SelectFile()
        elif choice == "e":
            modifying = False

            
if __name__ == '__main__':
    ModifiyEvents()
