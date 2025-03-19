import random 
var=random.randint(0,10)
print("Vamos a jugar un juego")
print("Voy a pensar un número del 1 al 10 y tienes que adivinarlo")
var2=int(input("Dime cual es ese número "))
while var2!=var:
    var2=int(input("no es correcto "))
else:
    print("correcto")