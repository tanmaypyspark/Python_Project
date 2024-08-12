import utils.clearScreen as clearScreen

class user:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    
    def login(self):
        print('User Login...')
    
    def logout(self):
        print('User Logout')
    
    def __auth(self):
        print('User Logout...')

class Student(user):
    def __init__(self, name,id,roll,marks):
        super().__init__(name,id)
        self.rollnumber = roll
        self.marks = marks

    def login(self):
        super().login()
        print('Student Login...')
s1 = Student('Tanmay',2,1,90)
# print(s1.name)
print(s1.login())
print(s1.logout())


##Followed innature
## Parent --> child
##Give us major benifit of code reusability

## We Inherit:
#       Non-private attributes
#       Non - private methods
#       Constructor [Other magic methods]

## We cannot access private attributes or methods of our parent class.
## Parent can not inherit from child, only child can inherit from parent

## super keyword--: super() keyword is used to access methods of parents from our childs
## Types Of Inheritance
# 1. Simple
# 2.Heirarchal 
# 3. Multilevel 
# 4. Multiple 
# 5. Hybrid