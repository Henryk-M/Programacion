#53. A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las 
#sumas y el número de repeticiones. Con While
num1=int(input("Introduce el primer numero: "))
num2=int(input("Introduce el segundo numero: "))
suma=int(num1+num2)
rep=1
total=suma
print(f"El resultado de la suma es: {suma}")
continuar=input("Deseas repetir la operación s/n: ")
while continuar=="s":
    num1=int(input("Introduce el primer numero: "))
    num2=int(input("Introduce el segundo numero: "))
    suma=int(num1+num2)
    print(f"El resultado de la suma es: {suma}")
    continuar=input("Deseas repetir la operación s/n: ")
    rep+=1
    total=total+suma
else:
    if continuar=="n":
        print("Resumen")
        print(f"La suma total es de: {total} y el numero de repeticiones es de: {rep}")
