#this is assingment 9
#the file they should insert is first.txt

#asking for input
usr_file = input('What file would you like to open? Inlcude the file that it is placed in: ')
xfiles = open(usr_file,'w')

#writing to file
line1 = ('This is my first file!\n')
xfiles.write(line1)
xfiles.close() 

#prompt to stall
wait = input('press enter when done editing')

#reading file
changed = open(usr_file)
reading = changed.read()
print(reading)
