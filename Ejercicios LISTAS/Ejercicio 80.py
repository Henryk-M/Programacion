#
lista=[]
num=""
num=input("Introduce un número: ")
lista=num.split(".")
if len(lista)==2:
    if lista[0].isnumeric() and lista[1].isnumeric():
        print("Es decimal")
    else:
        print("No es un número con decimales")

else:
    print("No es un número con decimales")
