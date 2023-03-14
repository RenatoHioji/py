x = lambda a, b : a * b * b**2 # Where a is a parameter for x.
print(x(5, 7))


#lambda inside a function

def myFunc(a):
    return lambda l: a * l**2
    
funcao = myFunc(9)
print(funcao(5))



exit()
