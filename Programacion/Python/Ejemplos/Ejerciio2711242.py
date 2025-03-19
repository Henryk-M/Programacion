var=input("Introduzca una palabra: ")
var1=input("dime una letra:")

for i in range(len(var)):
    if var1 in var[i]:
        print("La letra se encuentra en posición" , i+1)

        
        

