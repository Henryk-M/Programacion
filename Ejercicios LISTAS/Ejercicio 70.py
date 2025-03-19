#70. Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez 
#introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por 
#pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el 
#formato de entrada y salida tal y como se muestra en el testeo

lista1=[]
lista2=[]
times=int(input("Introduce el número de palabras que deseas introducir: "))
word=""
for word in range(times):
    word=input(f"Introduce la {word+1}ª palabra: ")
    lista1.append(word)
    lista2.append(word)
    lista2.reverse()
print(f"lista 1 contiene: {lista1}")
print(f"lista 2 contiene: {lista2}")