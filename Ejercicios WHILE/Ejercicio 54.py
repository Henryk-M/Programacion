#54. Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total 
#de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta 
#preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la 
#operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el 
#mensaje del acumulado es singular o plural.. . Con While
num1=int(input("Introduce el primer numero: "))
num2=int(input("Introduce el segundo numero: "))
suma=int(num1+num2)
rep=1
total=suma
print(f"El resultado de la suma es: {suma}")
print(f"El total acumulado es: {total} y llevas {rep} operacion realizada")
while total<50:
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