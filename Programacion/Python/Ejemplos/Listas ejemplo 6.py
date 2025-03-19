
val=input("Introduce los valores separados por guion: ")
lista=val.split("-")
listan=[]
listal=[]
for recorrer in lista:
    if recorrer.isnumeric():
        listan.append(recorrer)
    else:
        listal.append(recorrer)

print(lista)
print(listan)
print(listal)
lista3=[int(x) for x in listan]
print(sum(lista3))
