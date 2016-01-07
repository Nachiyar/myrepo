class person:
    def _init_(self):
        print "calling self"
        
class female(person):

    def getgender(self):
        print "female"

class male(person):

    def getgender(self):
        print "male"

f = female()
m = male()
f.getgender()
m.getgender()


    
