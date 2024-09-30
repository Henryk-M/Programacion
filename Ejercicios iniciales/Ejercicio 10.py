#10. Introduce por teclado dos números y muestre por pantalla la siguiente información: 
#cociente, resto y si el dividendo es par o impar.
var=float(input("Introduce el primer número"))

var2=float(input("Introduce el segundo número"))

var3=(var/var2)
print(f"El cociente es:{var/var2}")
print(f"El resto es:{var/var2-var3}")
if var%var2==0: print("El dividendo es: par")
else: print("El dividendo es: impar")


