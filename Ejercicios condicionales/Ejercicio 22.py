#22. Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. 
#Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.
n=float(input("Introduce tu nota"))
if n<0 or n>10 :
    print("La nota que has introducido no está entre 0 y 10")
else:
    if n<5 :
        print(f"Has sacado un {n} y has suspendido")
    if n>4 or n==5:
            print (f"Has sacado un {n} y has aprobado")
        
    
    
 
