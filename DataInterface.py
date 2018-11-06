#interface for loading and saving json lists of events

import simplejson as json

def SaveFile(events_list):
    try:
        events_json = json.dumps(events_list)
        with open('data.json', 'w') as write_file:
            json.dump(events_json, write_file)
        print("list saved")
        print(events_json)
    except Exception as e:
        print(e)

#TODO add file integrety check
def LoadFile(file_name):
    with open("data.json", "r") as read_file:
        return json.load(read_file)

def GetEventByDate():
    pass

def GetEventByName():
    pass

