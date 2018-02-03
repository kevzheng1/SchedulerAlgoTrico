from calendarclass import *
from class_course import *
from time_parser import *
from day_parser import *
from random import randint
import json

#open the json file and convert to python data type
file = open("Spring_2018.json", 'r')
Spring2018 = json.load(file)
#initiate lists for random number and courses
randNums = []
courses = []
#add 6 random numbers to randNums list
for i in range(8):
    randomNum = randint(0, 20)
    randNums.append(randomNum)
print(randNums)
#for each course in index dictated by RNG
#add the course to courses list
for rand in randNums:
    duration = Spring2018[rand]['Time And Days']
    name = Spring2018[rand]['Course Title']
    location = Spring2018[rand]['Room Location']
    weekday = duration.split(" ")[0]
    course = Course(name, weekday, duration, location)
    courses.append(course)
print(courses);


courseRequests = []
secondTestCal = Calendar()
print ("How many courses do you want to add?")
totalCourses = int(input())
for i in range(totalCourses):
    print ("Time for this course: ex. MWF 11:20am-12:35pm")
    courseRequests.append(Course("Test", input(), "Swarthmore"))
    if secondTestCal.addCourse(courseRequests[i].getStart_time(), courseRequests[i].getEnd_time()):
        print(secondTestCal.returnCal("blocks"))
    else:
        print("Conflict Detected!")
        break
print (courseRequests[0].getStart_time())
