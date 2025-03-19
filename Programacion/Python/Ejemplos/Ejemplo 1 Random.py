import random

numero=random.randint(1, 4)


minumero=int(input("introduce un numero: "))

while numero!=minumero:
    print("fallaste")
    minumero=int(input("has falllado, introduce otro numero: "))
else:
    print("El numero es correcto")