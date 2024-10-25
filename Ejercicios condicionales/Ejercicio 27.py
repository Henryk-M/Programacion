#27. Mejora el programa anterior para controlar que el valor introducido es una letra y en 
#caso de introducir un numero, aparezca un aviso por pantalla
txt=input("Introduce una letra ")
if txt.islower():
    print("La letra es minuscula")
if txt.isupper():
    print("La letra es mayuscula")
else:
    print ("El valor introducido es un numero")
    
