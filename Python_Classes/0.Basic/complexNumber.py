##Complex Number class is there for perform +,-,*,/,==,!=
import os
os.system('cls')

class ComplexNumber:

    def __init__(self,real=0.0,img=0.0):
        self.real = real
        self.img = img 
       # self.__complex = 

    def __str__(self):
        '''Convert to complex format'''
        if self.img<0:
            s = f'({self.real}{self.img}j)'
        else:
            s = f'({self.real}+{self.img}j)'
        
        if self.real == 0:
            return f'{self.img}j'
        return s
    
    def __add__(self,other):
        '''Add two complex number'''
        #print(cpx.real)

        real = self.real + other.real
        img = self.img +other.img
        return ComplexNumber(real,img)
    
    def __sub__(self,other):
        real = self.real -other.real
        img = self.img - other.img
        
        return ComplexNumber(real,img)
    
    def __mul__(self,other):
        # print(self)
        # print(other)

        realRreal = self.real * other.real
        realImg = self.real * other.img
        imgImg = self.img * other.img
        imgReal = self.img * other.real

        real = realRreal - imgImg
        img = realImg+imgReal

        return ComplexNumber(real,img)
    
    def __truediv__(self,other):
        
        numerator = self * other.conjugate()
        denominatorMul = other * other.conjugate()
        
        denominator = denominatorMul.real+denominatorMul.img
        
        real = numerator.real/denominator
        img = numerator.img/denominator
       
        return ComplexNumber(round(real,4),round(img,4))


    def conjugate(self):
        return ComplexNumber(self.real,-1*self.img)
        
    def __eq__(self,other):
        return (self.real ==other.real) and (self.img == other.img)
    
    def __ne__(self,other):
        return (self.real !=other.real) and (self.img != other.img)
              

# cp1 = ComplexNumber(3,4)
# cp2 = ComplexNumber(3,4)
#print(num.real,num.img)
#print(cp1)
# print('First Complex Number is:',cp1)
# print('Second Complex Number is:',cp2)
# print('Addition of two complex number is:',cp1+cp2)
# print('Subtraction of two complex number is:',cp1-cp2)
# print('Multiplication of two complex number is:',cp1*cp2)
# print('Div of two complex number is:',cp1/cp2)
# print('compare of two complex number is:',cp1 != cp2)
# print(f'Conjugate of {cp1} is:{cp1.conjugate()}')
# print(f'Conjugate of {cp2} is:{cp2.conjugate()}')
# print(num.sum())
# print(num.compare())

###__str__,__add__ --> This all are magic variables, conjugate is a method

#######################Test Case###########

complex1 = ComplexNumber(3,4)
complex2 = ComplexNumber(1,-2)
#print(complex1/complex2)
assert str(complex1) =="(3+4j)"
assert str(complex2) =="(1-2j)"
assert str(complex1+complex2) =="(4+2j)"
assert str(complex1-complex2) =="(2+6j)"
assert str(complex1*complex2) =="(11-2j)"
assert str(complex1/complex2) =="(-1.0+2.0j)"
assert complex1 != complex2