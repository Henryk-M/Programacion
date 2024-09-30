#16. Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El 
#resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un 
#resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso
#(raíz y división).
import math
var1=float(input("Introduce un número"))
var2=(math.sqrt(var1))
print(f"El resultado de la raiz cuadrada equivale a:{math.sqrt(var1)}")
print(f"El resultado de la división equivale a:{var2//2}")

