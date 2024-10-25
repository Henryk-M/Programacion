#20. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados 
#números entre 0 y 10
var1=int(input("Introduce el primer número"))
var2=int(input("Introduce el segundo número"))
if var1 < 0 or var1 > 10 or var2 < 0 or var2 > 10  :
    print("Uno o los dos números están fuera de los límites establecidos") 
else:
 if var1 < var2:
    print(f"El número {var1} es menor que el número {var2}")
 if var1 > var2:
    print(f"El número {var1} es mayor que el número {var2}")
 if var1==var2:
    print(f"El número {var1} es igual al número {var2}")