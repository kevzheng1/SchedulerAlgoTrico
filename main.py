from calendarclass import *
from class_course import *
from time_parser import *
from day_parser import *
from random import randint
from combinatorics import *
import json

#open the json file and convert to python data type
file = open("Spring_2018.json", 'r')
Spring2018 = json.load(file)

#store courses
courses = []
blacklist = ["Independent Study", "Directed Reading", "Honors Thesis", "Thesis",
            "Drawing II: Life Drawing"]

#get 8 random courses from the json
for i in range(8):
    rand = randint(0, 30)
    name = Spring2018[rand]['Course Title']
    #Independent Study classes have no day and time specified so don't retrive
    #them
    if name in blacklist:
        i -= 2
    else:
        duration = Spring2018[rand]['Time And Days']
        location = Spring2018[rand]['Room Location']
        course = Course(name, duration, location)
        courses.append(course)


courseRequests = courses
combos = course_comb(courseRequests)
for i in range(len(combos)):
    if len(combos[i]) == expected_combination(len(courseRequests), 4):
        print("")

'''
secondTestCal = Calendar()
print ("How many courses do you want to add?")
totalCourses = 8
for i in range(totalCourses):
    print ("Time for this course: and also day ex. 11:20AM-12:35PM")
    if secondTestCal.addCourse(courseRequests[i].getStart_time(), courseRequests[i].getEnd_time()):
        print(secondTestCal.returnCal("blocks"))
    else:
        print("Conflict Detected!")
        break
'''
