milista=[]
#para hacer una lista donde la variable se multiplica por dos
milista2=[]
numero=int(input("Introduce un número: "))
total=0
while numero!=0:
    milista.append(numero)
    #aqui esta
    milista2.append(numero*2)
    numero=int(input("Introduce otro número. teclea 0 para salir: "))
print(milista)
print(milista2)
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
print(sum(milista2))

#otra solucion para multiplicar por dos cada elemento
milista2=[x*2 for x in milista]
print(milista2)    
    