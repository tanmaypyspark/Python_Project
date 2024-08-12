# Having two or more methods (or functions) in a class with the same nae and different arguments(or paramenters)
import os
os.system('cls')
#from utils.clearScreen import *

class  User:

    def __init__(self, name, mobileNumber, address =""):
        if address =="":
            self.c1(name,mobileNumber)
        else:
            self.c2(name,mobileNumber,address)
    
    def c1(self, name,mobileNumber):
        self.name = name
        self.mobileNumber = mobileNumber
    
    def c2(self, name,mobileNumber,address):
        self.name = name
        self.mobileNumber = mobileNumber
        self.address = address

u1 = User('Tanmay','99999','Kolkata')
u2 = User('Rakesh','99999')
print(u1.name)
print(u2.name)
print(u1.address)
# print(u2.address)
