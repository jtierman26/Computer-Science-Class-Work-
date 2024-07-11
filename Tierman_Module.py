#this is my module 

int1 = int(6)
float2 = float(5.4321)
string2 = ftr("This is my string")

def funct1():
    print('The name of the function is: ' + funct1.__name__)
    
def funct2(int1):
    print('The name of the function is: ' + funct2.__name__)
    print(int1)
    
def funct3(string2):
    print('The name of the function is: ' + funct3.__name__)
    print(string2)
    return string2.upper()

def funct4(int1,string2):
    print('The name of the function is: ' + funct4.__name__)
    print(int1,string2)
    return int1, '_' ,string2
    
def funct5(int,float,str):
    print('5')
    return int1,'_',"%.2f"%float2,'_',string2
    
def globe():
    print(int1)
    print(float2)
    print(string2)
    
