numbers=input()
listas=numbers.split()

while len(listas)!=3:
    numbers=input()
    if numbers.isnumeric():
        listas.append(numbers)

listas=[int(x) for x in listas]    
print(sum(listas))