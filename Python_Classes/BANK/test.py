import os
os.system('cls')

class Test:
    __Number = 0

    def __init__(self,name, num):
        self.name = name
        self.number = num
    
    @property
    def getNum(self):
        return Test.__Number
    @getNum.setter
    def getNum(self,id):
        Test.__Number = id

t1 = Test('Tanmay',23)