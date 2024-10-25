#21. Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz 
#cuadrada no de un valor negativo
import math
a=int(input("Introduce el valor de a:"))
b=int(input("Introduce el valor de b:"))
c=int(input("introduce el valor de c:"))
raiz=b**2-4*a*c
if raiz<0:
    print("La raíz no puede ser un valor negativo")
else:
    x1=(-b+math.sqrt(raiz))/2*a
    print(f"El valor de x1 es:{x1}")
    x2=(-b-math.sqrt(raiz))/2*a
    print(f"El valor de x2 es:{x2}")




          