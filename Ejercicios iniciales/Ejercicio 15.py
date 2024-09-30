#15. Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, 
#introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.
import math
var1=math.pi
var2=float(input("Introduce el valor del radio del cilindro"))
var3=float(input("Introduce el valor de la altura del circulo"))
var4=round(2*var1*var2*var3+2*var1*var2**2,2)
var5=round(var1*var2**2*var3,2)
print(f"El valor del área del cilindro equivale a:{var4}")
print(f"El valor del volumen del cilindro equivale a:{var5}")





