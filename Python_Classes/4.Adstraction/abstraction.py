# Abstraction --> Abstract art -->Hidden
#  Fundamental concept of OOPS that involves hiding implementation details &showing only essnetial features
# Phone --> take call, make call
# similarly, we have a lot of exapmle in real life
# mobile, human body, tv remote 
###### How to use########
# from abc import ABC, abstractmethod
# we have to ensure 2 things
# 1. Inherit abc class
# 2. Should have an abstract method 
# So abstruction class are useful when we hae a group of related objects that should a common features
# but should/will have different implementation
import os
os.system('cls')

from abc import ABC, abstractmethod

class User(ABC):
    def __init__(self,name,mobileNumber,location):
        self.name = name
        self.mobileNumber = mobileNumber
        self.location = location
        
    @abstractmethod
    def login(self):
        pass
    
    def logout(self):
        print('Successfully logout!!')
    
    @abstractmethod
    def auth(self):
        pass
    
    
class Buyer(User):
    def __init__(self,bName,bmobileNumber,bauth,location):
        super().__init__(bName,bmobileNumber,location)
        self.__passCode = bauth
        self.__auth = False
    def login(self):
        self.auth()
        if self.__auth:
            print(f'User Name:{self.name}\nMobile Number:{self.mobileNumber}\nAuthentication Pass!')
        else:
            print(f'User Name:{self.name}\nMobile Number:{self.mobileNumber}\nAuthentication Failed!')

    def auth(self):
        if self.__passCode =='AAAA':
            self.__auth =True
        else:
            False
    
    def checkQty(self):
        print(f'Location:{self.location}\nNumber Of Quantity:100')
    
b1 = Buyer('Tanmay','999','AAAA11','Kolkata')
# print(b1.passcode)
# print(b1.authC)
b1.login()
 