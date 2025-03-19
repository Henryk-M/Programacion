#77. A partir de la lista del enunciado anterior, haz que el programa visualice por un lado las letras 
#y por otro los números permitiendo escoger orden ascendente o descendente. Como observarás 
#en la salida, el orden de las letras no es correcto, busca la manera de solucionarlo.
lista1=["a","b","D","x","r","X","3","h","w","2","i"]
listan=[]
listap=[]
leng=len(lista1)
for recorrer in lista1:
    if recorrer.isnumeric():
            listan.append(recorrer)
    if recorrer.isalpha():
            listap.append(recorrer)
    listan.sort()
    listap.sort()
visualize=int(input("Introduce 1 para visualizar en orden ascendente o 2 descendente: "))
if visualize==1:
    print(listan)
    print(listap)
if visualize==2:
    listan.sort(reverse=True)
    listap.sort(reverse=True)
    print(listan)
    print(listap)