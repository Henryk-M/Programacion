#82. Modifica el programa anterior para que sea el usuario intente adivinar la palabra escogida al 
#azar de la lista, indicando si es correcto o no. El programa debe no finaliza hasta que no se adivine 
#la palabra
import random
lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
value=random.choice(lista)
word=input("Introduce la palabra secreta: ")
while word!=value:
    print("SIGUE JUGANDO")
    word=input("Introduce la palabra secreta: ")
else:
    print("ACERTASTE")
    