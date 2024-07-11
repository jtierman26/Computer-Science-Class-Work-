#this is project 2

import Tierman_Module

def menu():
    print('1. Function 1 ')
    print('2. Function 2 ')
    print('3. Function 3 ')
    print('4. Function 4 ')
    print('5. Function 5 ')
    print('6. Display Global Variables ')
    print('7. Exit ')

def done():
    print('Goodbye!')
    quit()
    
def clearz():
    import os 
    print('Press Enter to Continue: ')
    os.system('cls')
    
while True:
    menu()
    pick = input('Please choose a number off the menu: ')
    try:
        choice = int(pick)
    except:
        print('This is not a number')
        quit()
        
    match choice:
        case 1:
            Tierman_Module.funct1()
            clearz()
        case 2:
            Tierman_Module.funct2(int)
            clearz()
        case 3:
            Tierman_Module.funct3()
            clearz()
        case 4:
            Tierman_Module.funct4()
            clearz()
        case 5:
            print('5')
        case 6:
            Tierman_Module.globe()
            clearz()
        case 7:
            done()
        