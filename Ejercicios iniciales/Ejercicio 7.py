#7. programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedes 
#forzar que el resultado de la división tenga 2 decimales?
var=float(input("Introduzca el primer operador"))
var2=float(input("Introduzca el segundo operador"))
print(f"La suma de operador1 y operador2 es:{var+var2}")
print(f"La resta de operador1 y operador2 es:{var-var2}")
print(f"La multiplicación de operador1 y operador2 es:{var*var2}")
var3=round(var/var2,2)
print(f"La división de operador1 y operador2 es:{var3}")
print(f"El exponente de operador1 y operador2 es:{var**var2}")
print(f"La división entera de operador1 y operador2 es:{var//var2}")

