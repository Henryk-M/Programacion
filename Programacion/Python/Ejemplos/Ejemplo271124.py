#ex 49 este es el 48, 
var=input("Introduzca una palabra")

for i in range(len(var)):
    var1=input("dime una letra:")
    if var1 in var:
        print("existe")
    else:
        print("la letra no existe")
    