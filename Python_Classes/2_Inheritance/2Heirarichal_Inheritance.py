import utils.clearScreen as clearScreen

class Grandfather:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def show_details(self):
        return f'Name:{self.name}, Age:{self.age}'
    def speak(self):
        return 'Grandfather speak wisly'

class Child1(Grandfather):
    def __init__(self, name, age, hobby) -> None:
        super().__init__(name, age)
        self.hobby = hobby

    def show_hobby(self):
        return f'Hobby:{self.hobby}'
    
    def speak(self):
        return 'Child1 speaks enthusiastically'

class Child2(Grandfather):
    def __init__(self, name, age, favorite_subject) -> None:
        super().__init__(name, age)
        self.favorite_subject = favorite_subject

    def show_favorite_subject(self):
        return f'Favorite subject:{self.favorite_subject}'
    
    def speak(self):
        return 'Child2 speaks thouhtfully.'

c1 = Child1('Alica',20,'painting')
c2 = Child2('Bob',22,'Math')
print(c1.show_details())
print(c1.show_hobby())
print(c1.speak())


print(c2.show_details())
print(c2.show_favorite_subject())
print(c2.speak())
## Both children get properties of parent
## Children are not releted to each other