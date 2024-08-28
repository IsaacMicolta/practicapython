"""frutas  = ["manzana", "peras", "uvas", "banano"]
numeros = [ 89, 87, 65, 78, 56]

frutas.append("sandia") #para agregar un elemento de la alista 
frutas.insert(0, "papaya") #para agregar un elemento en una posicion
frutas.extend(["mango", "kiwi", "lulo"]) #para agregar elementos a la listas 

frutas [8]= "mora" # editar un elemento de la lista 
frutas. remove ("papaya") #para eliminar un elemento 

del frutas [7] #para elimiar un elemento con la posicion
print (frutas)"""
"""frutasEliminadas = frutas.pop (1)
print (frutasEliminadas)"""

lista = []
while True:
    numeros= int (input ("Please insead a enter number: "))
    lista.append(numeros)
    si = input ("Do you wanna insead other enter number?:   ")
    print  ("your result is: ", sum(lista))
    if si == "no":
        break
print (f" your number are: ", lista)
        