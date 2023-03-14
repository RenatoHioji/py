#operator used in if  -> ==, != , <, <=, >, >=
a = 50
b = 20
c = 10
if a == b:
    print("a é igual a b.")
elif(a>b):
    print("a é maior que b.")
else:
    print("a não é maior nem igual a b.")

print("a é maior que b.") if a>b else print("a não é maior que b.")

print("A") if a>b else print("B") if b>a else print("A é igual a B") #short hand 3 condicionals.

if a>b and b>c:
    print("A é maior que B que é maior que C.")

if not a>b:
    print("a não é maior que b.")

if a > 10:
    print("A é maior que 10")
    if a > 30:
        print("E é maior que 30.")
        if a == 50:
            print("A é igual a 50.")
        else:
            print("A não é igual a 50.")
    else:
        print("Mas não é maior que 30")
        
else:
    print("A é menor que 10") 

#pass for empty if content
if a > b: 
    pass
exit()