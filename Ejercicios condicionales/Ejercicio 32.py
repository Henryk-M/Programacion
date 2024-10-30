#32. Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para 
#no distinguir entre mayúsculas y minúsculas
txt=("A quien madruga Dios lo ayuda.")
l=txt.lower()
usr=input("Introduce una palabra ")
x=usr.lower()
mrg=l.rfind(x)
if mrg==8 or mrg==16:
    print(f"La palabra esta en la frase y esta en el Indice {mrg}")
else:
    print("La palabra no esta en la frase")


