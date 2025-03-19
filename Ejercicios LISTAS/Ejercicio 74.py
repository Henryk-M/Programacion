#74. A partir del programa anterior, haz que se visualicen tanto las palabras que se repiten o no de 
#entre las 2 listas.
lista1=["casa","mesa","sal","sol","agua"]
lista2=["casa","luz","tres","tren","sol","pan"]
listarep=[]
listasingle=[]
listarepdef=[]
listasingledef=[]

for recorrer in lista1:
    if recorrer in lista2:
        listarep.append(recorrer)
    else:
        listasingle.append(recorrer)
for recorrer in lista2:
    if recorrer in lista1:
        listarep.append(recorrer)
    else:
        listasingle.append(recorrer)
listarepdef=set(listarep)
listasingledef=set(listasingle)
print(f"Estan repetidas:{listarepdef}")
print(f"No estan repetidas:{listasingledef}")