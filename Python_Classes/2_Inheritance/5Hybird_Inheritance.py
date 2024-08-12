#Mix of inheritance types
## Known as Diamond inheritance
import utils.clearScreen as clearScreen

class A:
    def show(self):
        return 'A'
class B(A):
    def show(self):
        return 'B'
class C(A):
    def show(self):
        return 'C'
class D(B,C):
        pass

obj = D()
print(obj.show()) ##