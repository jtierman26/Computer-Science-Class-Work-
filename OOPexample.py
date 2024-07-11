class Person:
    firstname   = ''
    lastname    = ''
    Doby        = 2000
    Dobm        = 1
    Dobd        = 1
    height      = 0
    ms          = None
    partnerFname    = ''
    partnerLname    = ''
    
    def _init_(self, fstname, lstname, ms=0,y=0,m=1,d=1,ht=0,pfn='',pln=''):
        #construcor
        self.firstname = fstname
        self.lastname  = lstname
        self.ms = ms
        #this is example of overloading
        self.Doby = y
        self.Dobm = m
        self.Dobd = d
        self.height = ht
        self.partnerFname = pfn
        self.partnerLname = pln
        
    def marries(self, fstname, lstname):
        self.partnerFname = fstname
        self.partnerLname = lstname
        self.ms = 1
    
    def divorces(self):
        self.partnerFname = ''
        self.partnerLname = ''
        self.ms = 0
        
    def partnerinfo(self)
        if self.partnerFname != '' and self.partnerLname != '' :
            print(self.partnerFname, self.partnerLname)
        else:
            print(self.firstname, self.lastname, 'is not married')
            

    def whoami(self):
        print(self.firstname, self.lastname)
        
#p1 = Person('john', 'doe')
    
class Professor(Person):
    cd           = ''
    dooy         = 2000
    doom         = 1
    dood         = 1
    specialty    = ''
    courses      = []
    
    def _init_(self, fname, lname):
        super()._init_(fname,lname)
    
    
    def addcourse(self, coursename):
        self.courses.append(coursename)
    
    
    def dropcourse(self, coursename):
        self.courses.remove(coursename)
        
    def listcourses():
        print(self.courses)

p = Person('mike', 'thomas')

print('Program Starts...')
prof1 = Professor('John', 'Doe')
prof1.whoami()
prof1.partnerinfo()
prof1.marries('Jane', 'Doe')
prof1.partnerinfo()
prof1.divorces()
prof1.partnerinfo()
print('2nd Step...')
prof1.addcourse('CS104')
prof1.addcourse('CS242')
prof1.addcoures('CS100')
prof1.dropcourse('CS100')
prof1.listcourses()
print('Exiting...')

    

