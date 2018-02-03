from calendarclass import *
from class_course import *

Bob = Calendar()
print(Bob.returnCal("blocks"))
for i in range(2):
    print("TEST: TYPE A STARTTIME AND ENDTIME")
    if Bob.addCourse(int(input()), int(input())) == False:
        print("Conflict Detected")
    print(Bob.returnCal("blocks"))
