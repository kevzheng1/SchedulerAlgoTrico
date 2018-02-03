from time_parser import *

class Course:
    # Input: name (str), weekday (str), start to end time (str) e.g. "11:20AM-12:35PM"
    # location (str)
    def __init__(self, name, weekday, duration, location):
        self.name       = name
        self.weekday    = weekday
        class_period = time_parser(duration)
        self.start_time = class_period[0]
        self.end_time   = class_period[1]
        self.location   = location
        # Start converting these weekdays str into list of start time and end time
        # Let's say we have MWF as our weekday input

    def getName(self):
        return self.name

    def getWeekday(self):
        return self.weekday

    def getStart_time(self):
        return self.start_time

    def getEnd_time(self):
        return self.end_time

    def getLocation(self):
        return self.location

    def __str__(self):
        result = "Course name: %s" %(self.name) + "\n" + self.weekday + "\n"
        result += str(self.start_time) + "\n" + str(self.end_time) + "\n"
        result += self.location + "\n"
        return result
