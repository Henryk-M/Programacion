#25. Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.
n=float(input("Introduce tu nota"))
if n<0 or n>10 :
    print("La nota que has introducido no está entre 0 y 10")
else: 
    if n>8.4 :
        print(f"Tu nota es un {n}, has sacado un excelente")
    if n<5:
        print (f"Tu nota es un {n}, has sacado un insuficiente")
    if n<8.5 and n>6.5:
        print (f"Tu nota es un {n}, has sacado un notable")
    if n<6.5 and n>5:
        print (f"Tu nota es un {n}, has sacado un satisfactorio")
