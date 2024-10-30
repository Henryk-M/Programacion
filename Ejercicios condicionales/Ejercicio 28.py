#28. Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza 
#elif.
txt=input("Introduce una letra ")
if txt.islower():
    print("La letra es minuscula")
if txt.isupper():
    print("La letra es mayuscula")
if txt.isnumeric():
    print ("El valor introducido es un numero")
else:
    print ("El valor introducido es un símbolo")
    
