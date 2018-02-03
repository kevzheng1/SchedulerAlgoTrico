from time_parser import *
from day_parser import *

class Course:
    # Input: name (str), weekday (str), start to end time (str) e.g. "11:20AM-12:35PM"
    # location (str)
    def __init__(self, name, time, location):
        self.name       = name
        time_lst        = time.split(" ")
        self.weekday    = time_lst[0]
        self.duration   = time_lst[1]
        self.location   = location
        # This part fixes the function.
        class_weekday   = weekday_parser(self.weekday)
        class_duration  = time_parser(self.duration)
        start_time      = class_duration[0]
        end_time        = class_duration[1]
        class_start_lst = []
        class_end_lst   = []
        five_min_num    = 288 # number of five-minute block every day
        n = len(class_weekday)
        for i in range(n):
            if class_weekday[i] == "M":
                class_start_lst.append(start_time)
                class_end_lst.append(end_time)
            elif class_weekday[i] == "T":
                class_start_lst.append(start_time + five_min_num)
                class_end_lst.append(end_time + five_min_num)
            elif class_weekday[i] == "W":
                class_start_lst.append(start_time + 2 * five_min_num)
                class_end_lst.append(end_time + 2 * five_min_num)
            elif class_weekday[i] == "H":
                class_start_lst.append(start_time + 3 * five_min_num)
                class_end_lst.append(end_time + 3 * five_min_num)
            elif class_weekday[i] == "F":
                class_start_lst.append(start_time + 4 * five_min_num )
                class_end_lst.append(end_time + 4 * five_min_num)
        # Now, the self part continues.
        self.start_time = class_start_lst
        self.end_time   = class_end_lst
        # Use self.start_time and self.end_time to change the boolean value
        # on the calendar

    def getName(self):
        return self.name

    def getWeekday(self):
        return self.weekday

    def getDuration(self):
        return self.duration

    def getLocation(self):
        return self.location

    def getStart_time(self):
        return self.start_time

    def getEnd_time(self):
        return self.end_time

    def __str__(self):
        result = "Course name: %s" %(self.name) + "\n" + self.weekday + "\n"
        result += str(self.duration) + "\n" + self.location + "\n\n"
        return result

def main():
    weekday_and_duration = "MWF 11:30AM-12:20PM"
    time_lst = weekday_and_duration.split(" ")
    print(time_lst)

main()
