#
#Create dated reminders that will notify you on your windows system task bar
#



class Reminder:
    # Message should be a string
    # date & time should be unix time
    def __init__(
        self,
        message = "Reminder message not set",
        date = 0,
        time = 0
    ):
        self.message = message
        self.date = date
        self.time = time

    def set_time(self,unixTime):
        self.time = unixTime

    def set_date(self,unixTime):
        self.date = unixTime

    def set_message(self,text):
        self.message = text

    def say(self,text):
        print(text)

a = Reminder()
a.say("Hello World!")

a.set_message("test message")
a.say(a.message)



