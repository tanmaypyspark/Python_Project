import utils.clearScreen as clearScreen

class Grandfather:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def show_details(self):
        return f'Name:{self.name}, Age:{self.age}'
    def speak(self):
        return 'Grandfather speak wisly'

class Father(Grandfather):
    def __init__(self, name, age, occupation) -> None:
        super().__init__(name, age)
        self.occupation = occupation

    def show_occupation(self):
        return f'Occupation:{self.occupation}'
    
    def speak(self):
        return 'Father speaks carefully'

class Child(Father):
    def __init__(self,name,age,occupation,hobby):
        super().__init__(name, age, occupation)
        self.hobby = hobby
    
    def show_hobby(self):
        return f'Hobby: {self.hobby}'
    
    # def speak(self):
    #     return 'Child speak excitedly'

f1 = Child('John',50,'Engineer','Cycling')

print(f1.show_details())
print(f1.show_occupation())
print(f1.show_hobby())
print(f1.speak())

## Lower levels gets properties from above levels
##super() of each class can reach out to just the parent