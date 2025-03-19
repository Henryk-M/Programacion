#71. Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en 
#esta lista no deben almacenarse las letras que se han introducido repetidas.
lista=[]
listdef=[]
proceed="s"
alpha=""
while proceed=="s":
    alpha=input("Introduce una letra: ")
    if alpha.isalpha():
        lista.append(alpha)
        proceed=input("¿Deseas continuar? s/n: ")
else:
    listdef=set(lista)
    print(listdef)


