import random
num=random.randint(1, 5)
mnum=int(input("Introduce un número: "))
if mnum<1 or mnum>5:
    print("El número introducido esta fuera de rango")
if mnum==num:
    print("Número acertado")
while num!=mnum:
    print("Número no acertado")
    mnum=int(input("Introduce otro numero: "))
    if mnum<1 or mnum>5:
        print("El número introducido esta fuera de rango")
else:
    print("Número acertado")