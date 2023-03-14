list = ["a", "b", "c"] #Are changeable and allow duplicates values.
listA = ["a", "b", "a", "c", "a"]

tuple = tuple(("Tuple", "Tuple")) #Can't be changed and allow duplicates values.

set = set({"olá", "Que tal?"}) #Don't have index, don't have organization and isn't organized.

print(list[-5:-1]) #lista inversa
print(type(tuple))
print(tuple[0:2])

#Checking existence.
if "a" in list:
    print("There is an a in the variable list")
    list.insert(2, "Olá") #Add something in a determined position.
    print(list)

list.append("Flw")
print(list)
listA.extend(list)
print(listA)

listA.remove("a")
print(listA)
listA.pop(5) #Remove an espefic index.
del listA[5] #The save as the above. 
listA.clear() #Limpa a lista.




#looping

for x in list:
    print(x)

for x in range(len(list)):
    print(list[x])



exit()
