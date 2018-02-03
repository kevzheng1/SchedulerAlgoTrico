""" Design choice: read from text files """
""" from class_course import * """

class Course:
    # Input: name (str), weekday (str), start to end time (str) e.g. "11:20AM-12:35PM"
    # location (str)
    def __init__(self, name, weekday, duration, location):
        self.name       = name
        self.weekday    = weekday
        self.duration   = duration
        self.location   = location
    def getName(self):
        return self.name

    def getWeekday(self):
        return self.weekday

    def getDuration(self):
        return self.duration

    def getLocation(self):
        return self.location

def main():
    things = read()
    for thing in things:
        print(thing.getName() + " " + thing.getWeekday() + " " + thing.getDuration() + " " + thing.getLocation())

def read():

    list = []
    name = ""
    weekday = ""
    duration = ""
    location = ""

    data = open('data.txt', 'r')

    i = 1
    for line in data:
        if (i%4 == 1):
            name = line
            i = i + 1
        elif (i%4 == 2):
            weekday = line
            i = i + 1
        elif (i%4 == 3):
            duration = line
            i = i + 1
        else:
            location = line
            obj = Course(name, weekday, duration, location)
            list.append(obj)
            i = i + 1

    data.close()

    return list

main()

"""
def write():
    name = str(raw_input("\nName of the course: "))
    weekday = str(raw_input("\nWeekday: "))
    duration = str(raw_input("\nDuration: "))
    location = str()
    obj = Course(obj, name, weekday, duration, location);
"""
