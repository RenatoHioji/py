mytuple = ("Apple", "Banana", "Abacaxi")
mystring = iter("Banana")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(mystring))
print(next(mystring))
print(next(mystring))
print(next(mystring))
print(next(mystring))

class iteracao:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <= 20:
            x = self.a 
            self.a += 1 
            return x
        else:
            raise StopIteration #Raise is used to talk about error or discontinuation AND StopIteration is used to stop de iter.
    
    
myiter = iter(iteracao())
i = 0
for x in myiter:
    print(x)

exit()