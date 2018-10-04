from datetime import date

today = date.today()
weekday = today.weekday()

##WeekDay##
# 0 - Monday
# 1 - Tuesday
# etc

with open("data.json", "r") as read_file:
    dats = json.load(read_file)

while True:
    
