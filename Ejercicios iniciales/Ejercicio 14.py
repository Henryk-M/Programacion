#14. Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área 
#y perímetro. Importa la librería match y utiliza el valor PI para hacer el cálculo. Redondea el 
#resultado a un decimal.
import math
var1=math.pi
var2=float(input("Introduce el valor del diámetro del circulo"))
var3=(var2/2)
var4=round(var1*var3**2,1)
var5=round(2*var1*var3,1)
print(f"El valor del área del circulo equivale a:{var4}")
print(f"El valor del perímetro del circulo equivale a:{var5}")

