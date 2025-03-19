#73. Diseña un programa que compruebe si los valores de la lista1 (casa,mesa,sal,sol,agua) están 
#repetidos o no en la lista2 (casa,luz,tres,tren,sol,pan). Haz que permita visualizar que palabras se 
#repiten y cuales no  
lista1=["casa","mesa","sal","sol","agua"]
lista2=["casa","luz","tres","tren","sol","pan"]
listarep=[]
listasingle=[]

for recorrer in lista1:
    if recorrer in lista2:
        listarep.append(recorrer)
    else:
        listasingle.append(recorrer)
print(f"Estan repetidas:{listarep}")
print(f"No estan repetidas:{listasingle}")