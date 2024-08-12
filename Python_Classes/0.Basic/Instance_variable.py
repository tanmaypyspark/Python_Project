import utils.clearScreen as clearScreen
class Student:
    NUMBEROFSTUDENT = 0
    SCHOOLNAME = 'SHS'
    def __init__(self, name, rollnumber, marks):
        numberOfStudent = 0
        self.__name = name
        self.__rollNumber = rollnumber
        self.__marks = marks
        self.numberOfStudent = Student.NUMBEROFSTUDENT+1
        Student.NUMBEROFSTUDENT= Student.NUMBEROFSTUDENT +1
    
    @property
    def details(self):
        return f'Hi My name is {self.__name} and my roll number is {self.__rollNumber} and my marks is {self.__marks}'

    @details.setter
    def details(self,name,rollnumber,marks):
        self.__name = name
        self.__rollNumber = rollnumber
        self.__marks = marks    
    
    def study(self):
        print(self.details(),'Im studing Arts')
    
    def play(Self):
        print('I\'\m gonna play')
    
s1 = Student('Tanmay', 1,90)
s2 = Student('Mayank',2,92)
print(s1.numberOfStudent)
print(s2.numberOfStudent)
##Here s1 & s2 are instance variable , which have different values of attribute
## numberOfStudent is instance property
##NUMBEROFSTUDEN & SCHOOLNAME is class property