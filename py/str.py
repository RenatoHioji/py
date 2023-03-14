#loop strings
x = "banana"
if "ana" in x:
    print("There is ana in banANA")
    
    
print("ana" in x) # Will return true because it has ana in banANA

print(len(x)) #print will write the length of X
for x in "banana": #in will return true if specified value is present in the object.
    print(x) #not in will return true if specified value is not present in the object.

#Upper = Maiúsculo lower = Minúsculo
x = "banana"
print(x.upper())
x = "BANANA"
print(x.lower())

x = "BANANA, IS, VERY, GOOD" 
print(x)
print(x.lower().strip()) #replace all blankspace to nothing.
print(x.replace("", "A")) #replace all blankspace to A.
print(x.split(",")) #Divide the sentence in list by ','.

x = "Banana"
y = "Is"
z = "Very Good"
c = x + " " + y + " " + z
print(c)

x = 18
X = 2004
y = "Olá mundo, tenho {} anos"
#Adição de números para strings, usando format e {}
if x >= 18:
    print(y.format(x) + " e sou maior de idade")

else:
    print (y.format(x)) 


#Usando index

y = "Olá mundo, tenho {0} anos e nasci em {1}"
print(y.format(x, X))

x = "They used to call me \"Ahiem\" " #Its necessary to use \ to add double quotes to a string.
x = "They call me something, but... \n Its necessary" #Breakline.
x = "They call me \t something" #   tab.
x = "They callm\b me" #Apaga o caracter anterior .
print(x)
print(x.count("a")) #Count how many a we have in x.
print(x.capitalize()) #Upper the first caracter in the sentence.
print(x.find("a")) #Find the position of A in x. -> se der erro o valor de output será -1.
print(x.index("\b")) #Find the position of A in x. -> se der erro o valor de output será de ValueError exception.


exit()

