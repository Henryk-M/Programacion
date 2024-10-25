#23. Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un 
#notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota 
#introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.
n=float(input("Introduce tu nota"))
if n<0 :
    print("La nota que has introducido no está entre 0 y 10")
if n>10 :
    print("La nota que has introducido no está entre 0 y 10")
else: 
    if n>8.4 :
        print(f"Tu nota es un {n}, has sacado un excelente")
    if n<5:
        print (f"Tu nota es un {n}, has sacado un insuficiente")
    if n<8.5:
        print (f"Tu nota es un {n}, has sacado un notable")
    if n<6.5:
        print (f"Tu nota es un {n}, has sacado un satisfactorio")