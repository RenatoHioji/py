#Comentário 
""" aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"""
print("Hello, World")


frutas = {"Maça", "Banana", "Uva"} #Colections uses {}
Z = z = frutas
print(Z, z)


X, x = "Tchau, Mundo ", "Olá Mundo"
print(X + x)
#X será diferente de x.

print(x) #print irá mostrar Olá Mundo



x = float(5)
y = 10
print(x) #print irá mostrar 5.0.
print(x + y)
print(type(x))



#for especifics types of data, we can use str() for string, int() for integers 
#and float() for real number .

#variável global
a = 5 # É uma variável global.
def myFunc():
    a = 7 #Não é uma variável global e não substitui a variável global.
    print("2 + 3 não é: ", a)
myFunc()
print(a)
#To create a global u need to use "global" on the function.
def teste():
    global b 
    b = 10
    print(b)
teste()
print(b)

#To change the variable's value, its need to use global too.
def teste2():
    global b 
    b = 12
    print(b)
teste2()






exit()
