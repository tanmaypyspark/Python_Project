import os
import datetime
from utility.bank_function import *


os.system('cls')

cwd = os.path.dirname(os.path.realpath(__file__))

class Setup:
    
    __USERDETAILS = get_conf(os.path.join(cwd,'DATA\\user_details.json'))

    # def __init__(self):
    #     if uType =='User':
    #         self.user(userName, accNo, passCode,)
    #     elif uType == 'Emp':
    #         self.employee(userName, passCode)
    
    # def user(self, userName, accNo, passCode):
    #     self.userName = userName
    #     self.accNo = accNo
    #     self.passCode = passCode

    # def employee(self,userName, passCode, otp='0000'):
    #     self.userName = userName
    #     self.passCode =passCode
        
    
    def login(self,uType):
        uPassCode = self.get[uType][self.userName]
        print('uPassCode',uPassCode)

    def createAcc(self,firstName, lastName,govt_id, mobileNumber, location, pincode, branchName):
        print('Well Come to the BNB!!\nPlease fill the mandatory field to create an account.')
        full_Name = firstName.upper() + ' ' + lastName.upper()
        id = f'U{firstName.upper()[0:2]}{lastName.upper()[0:2]}{getid()}{branchName.upper()[0:2]}'
        user_details = {
            'name':full_Name,
            'govt_id':govt_id,
            'mobileNumber':mobileNumber,
            'location':location,
            'pincode':pincode,
            'branchName': branchName.upper()
        }
        # print(id)
        # print(user_details)
        try:
            self.getUser= id, user_details
        except Exception as e:
            print(f'Error: An error is encounter while create the account, {e}')

        ##Save the data
        try:
            self.__savethedata()
        except Exception as e:
            print('Error: Server is down.\nTry after some time!!')
    @property
    def getUser(self):
        return Setup.__USERDETAILS 
    
    @getUser.setter
    def getUser(self,user_data):
        id, user_details = user_data
        if isinstance(user_details, dict) and isinstance(id, str):
            Setup.__USERDETAILS[id] = user_details
        else:
            print('ERRRRR')
    
    def __savethedata(self):
        #print(Setup.__USERDETAILS)
        writeConf(Setup.__USERDETAILS, os.path.join(cwd,'DATA\\user_details.json'))

class Admin(Setup):
    pass

class Users(Setup):

    def __init__(self,firstName = '', lastName='', govtID = '', mobileNumber='', location ='', pincode = '', brachName='',userName='',accNo='',passCode='', newAcc=True):
        #super().__init__(self)
        if newAcc:
            self.uNewAcc(firstName, lastName,govtID, mobileNumber, location, pincode, brachName)
        else:
            self.exAcc(userName,accNo,passCode)


    def uNewAcc(self,firstName, lastName, govtID, mobileNumber, location, pincode, brachName):
        self.firstName = firstName
        self.lastName = lastName
        self.govtId = govtID
        self.mobileNumber = mobileNumber
        self.location = location
        self.pincode = pincode
        self.branchName = brachName
    
    def exAcc(self, userName, accNo, passCode):
        self.userName = userName
        self.accNo = accNo
        self.passCode = passCode
    
    def createAcc(self):
        return super().createAcc(self.firstName, self.lastName, self.govtId, self.mobileNumber, self.location, self.pincode, self.branchName)
    
# u12 = Users()
u1 = Users('Akash', 'Mandal','FEUCM2343ER','1234543','Ankri','712402','Chiladangi')
u1.createAcc()
# print(u1.getUser)




# s1 = Setup('Tony','0123','090','User')
# print(s1.get)
##################### Start From Her ###########################
# print('Well Come TO The BNB')
# print(datetime.datetime.now())

# print('Please Choose the option!')

# option = int(input('For Existing Customer Type --> 1 .\nFor Create new account Type --> 2\nType Here: '))
# if option == 1:
#     print('App is Under developement!!')
# elif option == 2:
#     print('Please be handy all the documents listed below:\nName, Address, Pincode, Govt Id, Mobile Number, Pincode')
#     firstname = str(input('First name: '))
#     lastname = str(input('Last name: '))
#     print('Please Provide address:')
#     villTown= str(input('Vill/Town: '))
#     po = str(input('Post Office: '))
#     ps = str(input('Police Station: '))
#     land_Mark = str(input('Land Mark, if not provide please type NA: '))
#     pincode = str(input('Pincode: '))
#     dist = str(input('District: '))
#     state = str(input('State: '))

#     if land_Mark == 'NA':
#         address = f'vill:{villTown}, Post Office: {po}, Police Station: {ps}, District:{dist}, State: {state} Pincode: {pincode}'
#     else:
#         address = f'vill:{villTown}, Post Office: {po}, Police Station: {ps}, Land Mark: {land_Mark}, Pincode: {pincode}'
    
#     print('Address:', address)
