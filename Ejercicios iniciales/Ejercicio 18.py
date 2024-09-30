#18. Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan 
#importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores 
#de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por 
#teclado el número de menores y el número de adultos que asisten al cine.
var1=(12)
var2=int(input("Introduce el número de menores"))
var3=int(input("Introduce el número de adultos"))
print(f"El precio total del cine para {var2} menor/es es:{var1-var1*0.50}")
print(f"El precio total del cine para {var3} adulto/s es:{var1-var1*0.10}")

