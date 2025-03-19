numeros=input("Introduce los numeors separados por un espacio: ")
#split solo admite string, no numeros
listanumeros=numeros.split()
lista2=[]
print(listanumeros)

for contador in listanumeros:
    contador=int(contador)
#necesito convertitr otra vez los valores a int para poder efectuar la operacion

#lista2=[int(x)*2 for x in listanumeros]
#para eliminar los valores duplicados se usa el set
lista2=set(listanumeros)
print(lista2)
