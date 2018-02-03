from calendarclass import *
from class_course import *
from time_parser import *

courseRequests = []
secondTestCal = Calendar()
print ("How many courses do you want to add?")
totalCourses = int(input())
for i in range(totalCourses):
    print ("Time for this course: ex. 11:20AM-12:35PM")
    courseRequests.append(Course("Test", "M", input(), "Swarthmore"))
    secondTestCal.addCourse(courseRequests[i].getStart_time(), courseRequests[i].getEnd_time())
    print(secondTestCal.returnCal("blocks"))
