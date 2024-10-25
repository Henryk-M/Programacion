#26. Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si 
#está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.
txt=input("Introduce una letra")
if txt.islower():
    print("La letra es minúscula")
if txt.isupper():
    print("La letra es mayúscula")
else:
    print ("La letra es mayúscula ¿?")
