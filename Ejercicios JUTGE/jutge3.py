numbers=input()
listas=numbers.split()
listas=[int(x) for x in listas]
if len(numbers)<2:
    numbers=input()
    listas.append(numbers)
    listas=[int(x) for x in listas]
    
print(sum(listas))