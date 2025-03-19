password=input("Introduce un password de 8 letras: ")

while len(password)!=8:
    password=(input("Introduce de nuevo el password: "))
else:
    print("El password es correcto")
    