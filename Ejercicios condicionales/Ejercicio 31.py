txt=("A quien madruga Dios lo ayuda.")
usr=input("Introduce una palabra ")
mrg=txt.rfind(usr)
if mrg==8 or mrg==16:
    print(f"La palabra esta en la frase y esta en el Indice {mrg}")
else:
    print("La palabra no esta en la frase")

