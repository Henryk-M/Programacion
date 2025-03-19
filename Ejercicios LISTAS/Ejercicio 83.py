#83. Modifica el código del ejercicio anterior para que el programa permita repetir x partidas (hasta 
#que el usuario lo decida). Tienes que controlar una puntuación de cada partida de la siguiente 
#manera, si la palabra la aciertas a la primera son 8 puntos, si la aciertas a la segunda 7 puntos y así 
#sucesivamente.
#Una vez el usuario desea finalizar el programa tiene que sumar todas tus puntuaciones obtenidas. 
#Si el total supera la media de la puntuación posible de todas las partidas, se puede decir que la 
#suerte le acompaña, de lo contrario mejor no Se dediques a los juegos de azar . PISTA.. ¿existe 
#algún método que permita sumar el contenido de una lista?

import random
lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
score=[]
points=8
ypoints=0
games=0
value=random.choice(lista)
proceed="s"
while proceed=="s":
    word=input("Introduce la palabra secreta: ")
    if word!=value:
        print("SIGUE JUGANDO")
        points=points-1
        word=input("Introduce la palabra secreta: ")
    if word==value:
        print("ACERTASTE")
        ypoints=points
        score.append(ypoints)
        points=8
        games+=1
        value=random.choice(lista)
        proceed=input("¿Quieres jugar de nuevo? s/n: ")
else:
    totalscore=[int(x) for x in score]
    print (f"Puntuación: {score}")
    print ("Tu puntuación ha sido de:", (sum(totalscore)))
    avrage=sum(score)/len(score)
    print(f"La media de las partidas realizadas es de: {avrage}")
    if (sum(totalscore))>avrage:
        print("Tienes buena suerte")
    if (sum(totalscore))<avrage:
        print("Dedicate al parchís")
    