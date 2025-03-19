#la lista se define con corchetes: mi lista [1,2,3,4,5]
#una lista puede contener string y numeros a la vez, puede contener otra lista etc
#es igual a cuando utilizamos string, se puede aplicar a bucles 
#funciona con while y for 
#tiene sus propios metodos y unas funciones como split() len() sum()
#usar control+alt para sacar corchetes
#append() añade al final de la lista e inser() te deja seleccionar donde especificamente quieres añadir
#con el max ya puedo sacar el valor mas grande y min el mas pequeño de la lista
milista=[]
numero=int(input("Introduce un número: "))
total=0
while numero!=0:
    milista.append(numero)
    numero=int(input("Introduce otro número. teclea 0 para salir: "))
print(milista)
print(max(milista))
print(min(milista))
#para sumar los elementos de la lista, recorrer ira entrando en cada elemento de la lisrta yt lo sumara:
for recorrer in milista:
    total=total+recorrer

print(total)

#tambien se podria hacer asi:
for recorrer in range(0,len(milista)):
    total=total+milista[recorrer]
print(total)

#otra manera de hacerlo:
    
print(sum(milista))