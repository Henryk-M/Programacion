# 78. A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea 
#eliminar de la lista, siendo únicamente los números los valores permitidos para suprimir
lista1=["a","b","D","x","r","X","3","h","w","2","i"]
proceed="s"
while proceed=="s":
    remove=input("Introduce el valor que deseas eliminar: ")
    if remove.isalpha():
        remove=input("Introduce un valor númerico: ")
        
    if remove in lista1:
        lista1.remove(remove)
        print(lista1)
        proceed=input("¿Deseas introducir otro valor? s/n: ")
    else:
        print("El valor introducido no está en la lista")
        proceed=input("¿Deseas introducir otro valor? s/n: ")
        
    