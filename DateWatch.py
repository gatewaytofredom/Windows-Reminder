#detects if a current date and time is appropriete to make a popup message

from datetime import date

today = date.today()
weekday = today.weekday()

##WeekDay##
# 0 - Monday
# 1 - Tuesday
# etc

def CheckForEvent(event_list):
    dates = []
    for item in event_list:
        dates.append(item[0])
        
    print(dates)

