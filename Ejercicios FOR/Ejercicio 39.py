#39. Programa que pida n números y que, tras introducir el último número, debe aparecer por 
#pantalla el número total de positivos, negativos y número de 0.

var=int(input("Introduce la cantidad de números que deseas introducir: "))
ze=0
po=0
ne=0
for contador in range(0,var):
    num=float(input("Introduce un número: "))
    if num==0:
        ze=ze+1
    if num>0:
        po=po+1
    if num<0:
        ne=ne+1
        
print(f"La cantidad de números ceros es: {ze}") 
print(f"La cantidad de números positivos es: {po}") 
print(f"La cantidad de números negativos es: {ne}") 
                
            
    
    
        
    

