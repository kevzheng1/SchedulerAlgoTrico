class Calendar:
    def __init__ (self):
        self.valid = False
        blocks = []
        #TODO find how many five minute blocks in a five day week
        for i in range(50):
            blocks.append(False)
        self.blocks = blocks

    def returnCal(self, target):
        if target == "blocks":
            return self.blocks
        if target == "valid":
            return self.valid

    def addCourse(self, starttime, endtime):
        duration = endtime - starttime
        for i in range(starttime, endtime):
            if self.blocks[i] == True:
                self.valid = False
                return False
            else:
                self.blocks[i] == True
        return True

Bob = Calendar()
print(Bob.returnCal("blocks"))
print("TEST: TYPE A STARTTIME AND ENDTIME")
if Bob.addCourse(int(input()), int(input())) == False:
    print("Conflict Detected")
print(Bob.returnCal("blocks"))
