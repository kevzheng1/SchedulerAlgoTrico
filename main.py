from calendarclass import *
from class_course import *
from time_parser import *

testCal = Calendar()
testCourse = Course("Test", "M", "11:20AM-12:35PM", "Swarthmore")
testCal.addCourse(testCourse.getStart_time(), testCourse.getEnd_time())
print(testCal.returnCal("blocks"))
courseRequests = []
secondTestCal = Calendar()
print ("How many courses do you want to add?")
totalCourses = int(input())
for i in range(totalCourses):
    print ("Time for this course: ex. 11:20AM-12:35PM")
    courseRequests[i] = Course("Test", "M", input(), "Swarthmore")
    secondTestCal.addCourse(courseRequests[i].getStart_time(), courseRequests[i].getEnd_time())
    print(testCal.returnCal("blocks"))
