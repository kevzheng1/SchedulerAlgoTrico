from calendarclass import *
from class_course import *
from time_parser import *

testCal = Calendar()
testCourse = Course("Test", "M", 600, 1000, "Swarthmore")
testCal.addCourse(testCourse.getStart_time(), testCourse.getEnd_time())
print(testCal.returnCal("blocks"))
