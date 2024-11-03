#inicializo valores a cada variable
var_numero=str(6734)
#obtengo su longitud
var_longitud=len(var_numero)
#sumo cada digito a partir del índice de cada posición
var_suma=var_numero[0]+var_numero[1]+var_numero[2]+var_numero[3]
#utilizo una condición y el operador aritmético // para saber si el resto da 0 y ver si es par
var_suma=int(6+7+3+4)
if var_suma//2==0:
   print(f"el valor de {var_suma} es par")
else:
   print(f"el valor de {var_suma} es impar")
 