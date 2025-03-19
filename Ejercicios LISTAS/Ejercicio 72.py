#72. A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y 
#no deben almacenarse en la lista
lista=[]
listdef=[]
listn=[]
proceed="s"
alpha=""
while proceed=="s":
    alpha=input("Introduce una letra: ")
    if alpha.isnumeric():
        listn.append(alpha)
    if alpha in "aáà":
        alpha="a"
        lista.append(alpha)
    if alpha in "eéè":
        alpha="e"
        lista.append(alpha)
    if alpha in "iíì":
        alpha="i"
        lista.append(alpha)
    if alpha in "oóò":
        alpha="o"
        lista.append(alpha)
    if alpha in "uúù":
        alpha="u"
        lista.append(alpha)
    proceed=input("¿Deseas continuar? s/n: ")
else:
    listdef=set(lista)
    print(listdef)
    
