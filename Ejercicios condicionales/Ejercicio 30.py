frase=input("Introduce una frase ")
l=(len(frase))
if l==11:
    print(f"la frase tiene 11 caracteres")
if l<11:
    print("la frase tiene menos de 11 caracteres")
elif l>11:
    print("La frase tiene 11 o más caracteres")