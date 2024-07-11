#import the module containing class definitions/persons etc

import personnel

#no need to have these class definitions here, as they are imported from 
#personnel module

#class Person:
    #pass

#class Professor(Person):
    #pass

#class Student(Person):
    #pass


class SequenceIterator:

    def __init__(self, sequence=[]):
        self.seq = sequence  
        self.k = -1 
        
    def __seqnext__(self):
        self.k += 1 
        if self.k < len(self.seq):
            pass
        else:
            self.k = 0
        
        returnself.seq[self.k]
        
    def __next__(self):
        self.k += 1
        return self.k 
        
    def __reset__(self):
        self.k = -1
        
    def __iter__(self):
        return self

mylist = list()
mylist.append(Professor('jane', 'doe'))
mylist.append(Professor('josh', 'smith'))
mylist.append(Professor('zane'. 'dear'))
mylist.append(Professor('matt', 'gordon'))
mylist.append(Professor('diane', 'wolf'))


myiterator = SequenceIterator(mylist)

i = 10

while i >= 0:
    print(myiterator.__seqnext__())
    i += 1
    
print('Done')

