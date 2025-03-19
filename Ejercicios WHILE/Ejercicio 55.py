#55. Última vez que reutilizamos el mismo código.. lo prometo . A partir del programa anterior 
#haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y 
#cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While
num1=int(input("Introduce el primer numero: "))
num2=int(input("Introduce el segundo numero: "))
suma=int(num1+num2)
rep=1
total=suma
print(f"El resultado de la suma es: {suma}")
print(f"El total acumulado es: {total} y llevas {rep} operacion realizada")
while total<50 or total%2!=0:
    num1=int(input("Introduce el primer numero: "))
    num2=int(input("Introduce el segundo numero: "))
    suma=int(num1+num2)
    rep+=1
    total=total+suma
    print(f"El resultado de la suma es: {suma}")
    print(f"El total acumulado es: {total} y llevas {rep} operaciones realizadas")
else:
    print(f"El total acumulado es de: {total} y el numero de repeticiones es de: {rep}")
    print("Programa finalizado")