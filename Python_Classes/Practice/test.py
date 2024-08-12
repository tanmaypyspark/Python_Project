import os
os.system('cls')
class RunDefFileClean:
    

    def __init__(self,path, runtype):
        self.__csvPath = path
        self.__runtyp = runtype
        self.__goodtogo = False

        if self.__runtyp =='VACARVM_RESERVE':
            self.cfgstat = 'stat_mnt_run_status.ini'
        elif self.__runtyp =='VACARVM_SENSITIVITY':
            self.cfgstat = 'stat_adhoc_run_status.ini'
    
    

    def __del(self,*argv):
        #print('File in DEL:',os.path.join(self.__csvPath,file))
        try:
            for file in argv:
                os.unlink(os.path.join(self.__csvPath,file))
            return True
        except Exception as e:
            return f'Error: {e}'
        

    def __ExistingFile(self):
        for file in os.listdir(self.__csvPath):
            
            if self.__runtyp in file:
                print('File:',file)
                r = self.__del(file,self.cfgstat)
                if r:
                    self.__goodtogo = True

    @property
    def flag(self):
        self.__ExistingFile()
        return self.__goodtogo

path = 'C:\Test\Data'
runtype = 'VACARVM_SENSITIVITY'
# for file in os.listdir(path):
#     print(file)
obj1 = RunDefFileClean(path,runtype)
obj1.run()
