texto="Hola me llamo Alets y hoy tengo sueño y frio"

milista=[]
#para mandar el texto a una lista, lo que yo determine con simbolos como una coma todo lo que haya antes lo pone en una posicion 
milista=texto.split()
print(milista)
print(len(milista))
#quiero que el usuario despues d ehacer el split, que pueda buscar una palabra en la frase para contar las que aparecen en la frase
palabra=input("Pon la palabra que quieres buscar: ")
conteo=milista.count(palabra)
print(conteo)