#while contador<=5
#print(contador)
#contador+=1
#
#
#
contador=1
contPar=0
while contador<21:
    contador+=1
    if contador%2==0:
        contPar=contPar+1
        print("el numero par es: ", contador)
else:
    print("finalizado")

print("el total de pares es: ", contPar)