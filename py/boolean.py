#Only empty string, lists, tuple, etc., none and 0 is going to show false. Otherwise, it is going to output true.
print(bool([]))


class myclass():
    def __len__(self):
        return 0 
myobj = myclass()
print(bool(myobj)) #Irá retornar FALSE, pois o valor será 0.

def myFunc():
    return True
myFunc()
print(bool(myFunc()))

if myFunc():
    print("É TRUEEEEEEEEEEEE")
else:
    print("NÃOOOOOOOOOOOOOOOO")
    
x = 200
print(isinstance(x, int))
    
exit()