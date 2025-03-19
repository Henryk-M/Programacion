#37. Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado 
#o suspendido.

var=int(input("Introduce el número de notas que deseas introducir: "))
for contador in range(0,var):
        nota=float(input("Introduce una nota "))
        if nota>=5:
            print("Aprobado")
        if nota<5:
            print("Suspendido")
