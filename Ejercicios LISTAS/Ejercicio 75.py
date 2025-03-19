#75. Crea una lista con el siguiente nombre lista1 y su contenido: a,b,D,x,r,X,3,h,w,2,i. Presenta por 
#pantalla los siguientes resultados:
lista1=["a","b","D","x","r","X","3","h","w","2","i"]
leng=len(lista1)
nvalue=0
nalpha=0
nupper=0
suma=0

for recorrer in lista1:
    if recorrer.isnumeric():
        nvalue+=1 
        suma+=int(recorrer)
    
    if recorrer.isalpha():
        nalpha+=1
    if recorrer.isupper():
        nupper+=1
    
        
print(f"Número de valores: {leng}")
print(f"Cantidad de números: {nvalue}")
print(f"Cantidad de letras: {nalpha}")
print(f"Cantidad de mayúsculas: {nupper}")
print(f"Suma total: {suma}")
