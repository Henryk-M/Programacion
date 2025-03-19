#36. Programa que sume los n primeros números naturales. n Lo introduce el usuario.
var=int(input("Intoduce un número"))
total=0
for contador in range (var):
    total=total+(contador+1)
print(total)    
