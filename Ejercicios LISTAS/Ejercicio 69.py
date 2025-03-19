#69. Realiza un programa que permita introducir una cantidad exacta de números, cada número se 
#irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números 
#ordenados de menor a mayor.
times=int(input("Introduce la cantidad de números: "))
number=""
lista=[]
for number in range(times):
    number=int(input("Introduce un número: "))
    lista.append(number)
print(lista)