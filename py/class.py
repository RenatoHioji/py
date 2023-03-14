class Blackqueen:
    def __init__(peace, name,  moviment, color):
        peace.name = name
        peace.moviment = moviment
        peace.color = color
    def ___str___(peace):
        return f"{peace.name}{peace.moviment}{peace.color}"
p1 = Blackqueen("Queen", "X", "Black" )
print(p1.name, p1.moviment, p1.color)


class Whitequeen:
    def __init__(self, name,  moviment, color):
        self.name = name
        self.moviment = moviment
        self.color = color
    def __str__(self): #To set what the function will return when called, you can use __str__ for strings returns.
        return f"{self.name}{self.moviment}{self.color}" 


p2 = Whitequeen("Queen ", "X ", "White")
print(p2)

class Object:
    def __init__(self, name):
        self.name = name
    def myFunc(self):
        print("Olá, seja bem-vindo: ", self.name) #A method, an object that has a function

p3 = Object("Ahiem")
p3.myFunc() #Calling just the function in the class.
p3.name = "Ahiem2" #Changing the p3 name to Ahiem2.
p3.myFunc()
del p3.name #Deleting the name.
del p3 #Deleting the object.
exit()


