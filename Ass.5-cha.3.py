class Student:
    def __init__(self):
        self.__name = "name"
        self.__rollNumber = "rollNumber"

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

    def getRollNumber(self):
        return self.__rollNumber
s = Student()
s.setName("Raji")
s.setRollNumber("52")
print(s.getName()) 
print(s.getRollNumber())    
