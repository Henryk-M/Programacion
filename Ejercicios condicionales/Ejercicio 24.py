#24. Corrige los errores del siguiente codigo y comprueba que se ejecuta correctamente
var1=float(input("Introduce el peso: "))
var2=float(input("Introduce la altura: "))
var_imc=float(var1 / var2**2)
print(f"Si pesas {var1} kilos y mides {var2}, tu IMC es: , {var_imc}")
if var_imc > 25:
 print("Hay sobrepeso")
else:
 print("Estas dentro de los parametros normales")

