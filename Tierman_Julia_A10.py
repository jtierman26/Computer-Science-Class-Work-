#this is assingment 10
#menu function
def menu():
    print('1. Display File in UpperCase')
    print('2. Open File and Print in UpperCase to Another File')
    print('3. Find Average of the Floating Point Number Following DSPAM')
    print('4. Exit')
    
#start display function
def start():
    print('Welcome To My Files Program!')

#first menu option
def openUpper():
    xfiles = open('mbox_short.txt')
    for line in xfiles:
        remove = line.rstrip()
        print(remove.upper())
    
#second menu option
#using the with statment allows us to make sure that we can open both 
#files and write to the second one without any bugs it also will automatically close the file
#and the code looks cleaner (replaces the try and except)
def newUpper():
    with open('mbox_short.txt','r') as firstfile, open('mbox_short_upperc.txt', 'a') as secondfile:
    #making data in first file uppercase and sending it to second file
        for line in firstfile:
            secondfile.write(line)
            remove = line.rstrip()
            print(remove.upper())
#third menu option
def countSum():
    first = open('mbox_short.txt')
    find = []
    for line in first:
    #finding float number that follows DSPAM
        if line.strip().startswith('X-DSPAM-Confidence'):
            numb = float(line.split(':')[1].strip())
            find.append(numb)
    ave = sum(find)/len(find)
    print('The Average Spam Confidence is: ', ave)

#close function
def done():
    print('GoodBye! Have A Great Day!')
    quit()

#clear function
def clearz():
    import os
    input('Press Enter to Continue')
    os.system('cls')

#while true loop
while True:
    start()
    menu()
    pick = input('Please Choose a Number From the Menu: ')
    
    try:
        choice = int(pick)
    except:
        print('This is not a number')
        quit
    
    if choice == 1:
        openUpper()
        clearz()
    elif choice == 2:
        newUpper()
        clearz()
    elif choice == 3:
        countSum()
        clearz()
    elif choice == 4:
        done()