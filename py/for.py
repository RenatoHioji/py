fruits = ["Abacaxi", "Morango", "Laranja"]
for x in fruits:
    if x == "Morango":
        continue
    if x == "Laranja":
        break
    print(x)

#range

for x in range(6):
    print(x)

for x in range(2, 6): #The first number is where the for loop will start counting.
    print(x)
for x in range(2, 6, 3): #To add the step to for loop, its needed to add a third number.
    print(x)
else:
    print("O número x é maior que 6")

for x in fruits:
    for y in "Morango":
        print(x, y)

for x in fruits:
    for x in "Morango": #Will do X, Y and it's going to do Y and the last member of Y.
        print(x, y)
    
#We also can use pass to empty for.

exit()


