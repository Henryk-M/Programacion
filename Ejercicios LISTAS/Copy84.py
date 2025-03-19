#

import random
lista=["casa","barco","gato","perro","madera","agua","puente","pantalón"]
listal=[]
palabra=random.choice(lista)
listmess=[]
#modo a de cómo introducir cada letra en una posición de la lista
#for recorrer in palabra:
    #listal.append(recorrer)
#modo b que es separar las letras con un simbolo como por ejemplo el guion para luego pasar con el split a una lista 
separada="-".join(palabra)
listal=separada.split("-")

while len(listal)>0:
    letra=random.choice(listal)
    listmess.append(letra)
    listal.remove(letra)
wordmess="".join(listmess)
print("Adivina la palabra oculta: ",wordmess)
user=input("Introduce la palabra")
while user!=palabra:
    print("error, no es correcto")
    usuario=input("introduce la palabra: ")
else:
    print("has ganado")