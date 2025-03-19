#56. Realiza un programa que gestione un establecimiento de venta de bocadillos. Un pedido se 
#compone de: bocadillo, acompañamiento y bebida. Un cliente puede pedir más de un pedido. El 
#dependiente a partir del menú (ver imagen), se encarga de introducir los datos. El menú solo se 
#visualiza una vez al ejecutar el programa. El programa debe preguntar al dependiente tras la 
#realización de un pedido, si quiere gestionar otro.
orders=0
oderp1=0
orderp2=0
orderp3=0
totalpedido=0
percentage=0
totalconiva=0
discount5=0
discount15=0
totalcondescuento=0


print("MENÚ")
print("1. Bocadillo de calamares- 9 €")
print("2. Bocadillo de chistorra- 4.5 €")
print("3. Bikini de jamón- 2.5 €")
print("ACOMPAÑAMIENTO")
print("1. Patatas finas- 1.5 €")
print("2. Patatas gruesas- 1.75 €")
print("3. Patatas rústicas- 2€")
print("BEBIDAS")
print("1. Coca cola- 2 €")
print("2. Aquarius- 1.5 €")
print("3. Agua- 1 €")

repeat=input("¿Desea ordenar?: ")
while repeat=="s":
    orderp1=int(input("Elija el bocata: "))
    if orderp1==1:
        totalpedido=totalpedido+9
    if orderp1==2:
        totalpedido=totalpedido+4.5
    if orderp1==3:
        totalpedido=totalpedido+2.5
    orderp2=int(input("Elija el acompañamiento: "))
    if orderp2==1:
        totalpedido=totalpedido+1.5
    if orderp2==2:
        totalpedido=totalpedido+1.75
    if orderp2==3:
        totalpedido=totalpedido+2
    orderp3=int(input("Elija la bebida: "))
    if orderp3==1:
        totalpedido=totalpedido+2
    if orderp3==2:
        totalpedido=totalpedido+1.5
    if orderp3==3:
        totalpedido=totalpedido+1
    orders+=1
    repeat=input("¿Desea ordenar otra vez?: ")
else:
    print("RESUMEN")
    print(f"Numero de pedidos: {orders}")
    print(f"El total a pagar es: {totalpedido}")
    percentage=totalpedido*0.10
    totalconiva=totalpedido+percentage
    round(totalconiva,2)
    print(f"El total con IVA es: {totalconiva}")
    if totalconiva>19 and totalconiva<31:
        discount5=totalconiva*0.05
        totalcondescuento=totalconiva-discount5
        totalcondescuento=round(totalcondescuento,2)
        print(f"El total con descuento es: {totalcondescuento}")
    if totalconiva>30:
        discount15=totalconiva*0.15
        totalcondescuento=totalconiva-discount15
        totalcondescuento=round(totalcondescuento,2)
        print(f"El total con descuento es: {totalcondescuento}")
        
    
    
        
    