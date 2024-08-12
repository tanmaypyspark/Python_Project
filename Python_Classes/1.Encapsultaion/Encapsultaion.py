import utils.clearScreen as clearScreen
import json
class Student:
    __NUMBEROFSTUDENT = 0 #Class variable or static property
    __SCHOOLNAME = 'SHS'
    def __init__(self, name, rollnumber, marks):
        self.__name = name
        self.__rollNumber = rollnumber
        self.__marks = marks
        self.numberOfStudent = Student.__NUMBEROFSTUDENT+1
        Student.__NUMBEROFSTUDENT= Student.__NUMBEROFSTUDENT +1
    
    @property
    def details(self):
        return f'Hi My name is {self.__name} and my roll number is {self.__rollNumber} and my marks is {self.__marks}'

    @details.setter
    def details(self,value):
        # print(json.loads(value))
        dict_ = json.loads(value)
        
        if dict_['passcode'] ==self.__auth():
            self.__name = dict_['name']
            self.__rollNumber = dict_['rollnumber']
            self.__marks = dict_['marks']
        else:
            print('ACCESS DENIED!!')
    
    def __auth(self):
        return 'AUTH'
    
    @staticmethod #decorator
    def getSchoolName():
        return Student.__SCHOOLNAME
    
    @staticmethod
    def setSchoolName(newSchool,passcode):
        Student.__sendMail()
        Student.__SCHOOLNAME = newSchool
    
    @staticmethod
    def __sendMail():
        print('Sending mail to all the commite member...')
s1 = Student('Tanmay', 1,90)
s2 = Student('Mayank',2,92)

print(s1.details)
input_ = {
    'name':'Tanmay',
    'rollnumber':1,
    'marks':94,
    'passcode':'AUTH'}

s1.details=json.dumps(input_)
print(s1.details)

print(s1.getSchoolName())
s1.setSchoolName('SHY','0000')

# print(s1.numberOfStudent)
# print(s2.numberOfStudent)

##Encapsulation: The binding of our data members/ attributes and  methods in a single unit is known as encapsulation.
## Here we use __auth, __sendMail, __NUMBEROFSTUDENT, __name--> to hide from the end users, this is called binding

##Note: we can have static method which is not a method of class objects but method of class, @staticmethod. 
# own by class majorly but accessable by objects also