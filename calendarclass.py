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
        for i in range(len(starttime)):
            for j in range(int(starttime[i]), int(endtime[i])):
                if self.blocks[j] == True:
                    self.valid = False
                    return False
                else:
                    self.blocks[j] = True
        return True

# empties a stretch of time on the calendar
# mainly for debugging purposes
    def removeCourse(self, starttime, endtime):
        for i in range(starttime, endtime):
            self.blocks[i] = False
