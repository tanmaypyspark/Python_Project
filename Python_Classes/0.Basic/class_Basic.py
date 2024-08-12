import os
os.system('cls')

class Employee:
    ##Class is a blue print of creating instances
    def __init__(abc, first_name:str, last_name:str, email:str, salary:int):
        abc.firstName = first_name
        abc.lastName = last_name
        abc.email = email
        abc.salary = salary
        #conact
        abc.name = abc.firstName+' '+abc.lastName

# emp1 = Employee()
# emp2 = Employee()
# # emp1 & emp2 is the instances/objects of Employee calss.
# print(emp1)
# emp1.first = 'Tanmay'
# emp1.last = 'Mandal'
# emp1.email = 'tanmaym.mandal@gmail.com'
# emp1.salary = 40000

emp1 = Employee('Tanmay','Mandal','tanmaym.mandal@gamil.com',40000)
print(emp1.name)