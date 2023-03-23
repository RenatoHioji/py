#Scope is the area that a variable can be used.
def myFunc():
    a = 5 #a can't be used outside here.
    def myFunc2():
        print(a)
        #But a can be used here.
    myFunc2()
myFunc()