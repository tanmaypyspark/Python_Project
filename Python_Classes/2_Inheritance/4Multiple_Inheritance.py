## Not allowed in Java
## Ambeiguty solved in rhe order of inheritance, get properties of both parent
## MRO (method resolution order) follwed in resolving ambiguity

import utils.clearScreen as clearScreen

class Father:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def show_details(self):
        return f'Name:{self.name}, Age:{self.age}'
    
    def speak(self):
        return 'Father speaks carefully'
class Mother:
    def __init__(self, name, favorite_food):
        self.name = name
        self.favorite_food = favorite_food
    def show_favorite_food(self):
        return f'Favorite Food:{self.favorite_food}'
    
    def speak(self):
        return 'Monther speaks lovingly'
    
class Child(Father, Mother):
    def __init__(self, f_name,m_name,age,favorite_food,hobby):
        Father.__init__(self,f_name, age)
        Mother.__init__(self,m_name,favorite_food)
        self.hobby = hobby
    
    def show_hobby(self):
        return f'Hobby:{self.hobby}'
    
    def speak(self):
        return f'Child speaks excitedly'
    
f1 = Child('Daisy','Liza',16,'pizza', 'Dancing')
print(f1.show_details())
print(f1.show_favorite_food())
print(f1.show_hobby())
print(f1.speak())
print(f1.name)

print(Child.mro())