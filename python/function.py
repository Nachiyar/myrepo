def quadcube (x):
    return x**2, x**3
    
    
def function (name, project):
    print "Hi %s, Welcome to %s" % (name, project)

    
a, b = quadcube(3)
print a
print b
function(raw_input("Enter your name:"),raw_input("Enter the project:"))
