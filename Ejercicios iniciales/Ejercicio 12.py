#12. Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor 
#y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.
var1=float(input("Introduzca el valor del lado del trapecio"))
var2=float(input("Introduzca el valor de la base menor del trapecio"))
var3=float(input("Introduzca el valor de la base mayor del trapecio"))
var4=float(input("Introduzca el valor de la altura del trapecio"))
var5=(var3+var2)
print(f"El perimetro equivale a:{var3+var2+var1+var1}")
print(f"El área equivale a:{var5/2*var4}")
