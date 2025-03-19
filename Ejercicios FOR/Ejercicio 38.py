#38. A partir del programa anterior, establece los rangos para que el usuario no pueda introducir 
#notas inferiores a 0 y superiores a 10
var=int(input("Introduce el número de notas que deseas introducir: "))
for contador in range(0,var):
    nota=float(input("Introduce una nota "))
    if nota<0 or nota>10:
        print("Has introducido una nota equivocada")
    else:
        if nota>=5:
            print("Aprobado")
        if nota<5:
            print("Suspendido")

