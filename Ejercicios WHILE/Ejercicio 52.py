#52. Realiza un programa que sume dos números enteros por teclado y presente el resultado por 
#pantalla. El programa preguntará si deseas o no repetir la operación. Con While
num1=int(input("Introduce el primer numero: "))
num2=int(input("Introduce el segundo numero: "))
suma=int(num1+num2)
print(f"El resultado de la suma es: {suma}")
continuar=input("Deseas repetir la operación s/n: ")
while continuar=="s":
    num1=int(input("Introduce el primer numero: "))
    num2=int(input("Introduce el segundo numero: "))
    suma=int(num1+num2)
    print(f"El resultado de la suma es: {suma}")
    continuar=input("Deseas repetir la operación s/n: ") 
else:
    if continuar=="n":
        print("Programa finalizado")