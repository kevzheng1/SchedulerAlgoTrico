from calendarclass import *
from class_course import *
from time_parser import *
from day_parser import *
import json

Spring2018 = json.load(open("Spring_2018.json"))
print(Spring2018[0].keys)

courseRequests = []
secondTestCal = Calendar()
print ("How many courses do you want to add?")
totalCourses = int(input())
for i in range(totalCourses):
    print ("Time for this course: and also day ex. 11:20AM-12:35PM")
    courseRequests.append(Course("Test", input(), input(), "Swarthmore"))
    if secondTestCal.addCourse(courseRequests[i].getStart_time(), courseRequests[i].getEnd_time()):
        print(secondTestCal.returnCal("blocks"))
    else:
        print("Conflict Detected!")
        break
print (courseRequests[0].getStart_time())
