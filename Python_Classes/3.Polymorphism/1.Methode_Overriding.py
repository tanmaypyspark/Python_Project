#occurs when a subclass (child class) has the same method as the parent class
import os
os.system('cls')

class Animal:
    def sounds(self):
        print('Some Sounds')

class Dog(Animal):
    def sounds(self):
        print('Brak')

d1 = Dog()
print(d1.sounds())
d2 = Animal()
print(d2.sounds())