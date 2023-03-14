def myFunc():
    print("This is a function")

myFunc()

def myFunc(name = "Hioji"): #"Hioji" creates a default parameter, that will be used when the function has no arguments.
    print(name + " Tobi.")
myFunc("Nome")

#For unknown number of arguments, we should use * before the parameter, creating, then, a tuple of arguments.
def myFunc(*name):
    for x in name:
        print("O nome é: " + x)
myFunc("Renato", "Hioji", "Okamoto", "Odake")

def myFunc(w1, w2, w3):
    print(w1)

myFunc(w1="Olá", w2="Tchau", w3="Fui")

#for unknown number of arguments, use **, to always search for an especific arguement.
def myFunc(**name):
    return name['lname']
print(myFunc(fname = "Renato", lname = "Odake")) #to use a return value.
#we can also use pass to skip the empty function.

def myFunc(teste):
    if teste == 120:
        print("Tudo certo!")
    elif teste == teste:
        teste2 = teste + teste**2
        print(teste2)
    else: print("Error.")
myFunc(1)
exit()