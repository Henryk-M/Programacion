#17. Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado el 
#peso (en kg) y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado 
#es igual o superior a 25, debe aparecer un mensaje informando de sobrepeso.
var1=float(input("Introduce el valor de tu peso en kg"))
var2=float(input("Introduce el valor de tu estatura en metros"))
var3=(var1/var2**2)
if var3==25 or var3>25: print(f"Si pesas{var1} y mides {var2},tu IMC es de:{var3}.Hay sobrepeso")
else: print(f"Si pesas{var1} y mides {var2},tu IMC es de:{var3}")
