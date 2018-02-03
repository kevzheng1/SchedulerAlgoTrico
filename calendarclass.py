# defines class for a calendar of a single week M-F
class Calendar:
    def __init__ (self):
        self.valid = False
        blocks = []
        for i in range(1440):
            blocks.append(False)
        self.blocks = blocks

# returns target field from class Calendar
    def returnCal(self, target):
        if target == "blocks":
            return self.blocks
        if target == "valid":
            return self.valid

# adds a course to Calendar based on start time and end end_time
# where both are measured in blocks of 5 minutes
    def addCourse(self, starttime, endtime):
        duration = int(endtime - starttime)
        for i in range(starttime, endtime):
            if self.blocks[i] == True:
                self.valid = False
                return False
            else:
                self.blocks[i] = True
        return True

# empties a stretch of time on the calendar
# mainly for debugging purposes
    def removeCourse(self, starttime, endtime):
        for i in range(starttime, endtime):
            self.blocks[i] = False
"""
Bob = Calendar()
print(Bob.returnCal("blocks"))
for i in range(2):
    print("TEST: TYPE A STARTTIME AND ENDTIME")
    if Bob.addCourse(int(input()), int(input())) == False:
        print("Conflict Detected")
    print(Bob.returnCal("blocks"))
"""
