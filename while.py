"""dia= 0
semana= ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
while dia <7 :
    print("Hoy es: " , semana[dia])
    dia += 1"""

"""contador = 1 
while contador <=10:
    print (contador)
    contador += 1

contador = 1
while (contador <= 5):
    contador = contador + 1
    print("iteracion numero", contador)"""

"""contador = 0
while contador <5: 
    contador += 1
    print( "iteracion", contador)
    if contador == 3:
        break
    print ("game over")"""

"""print ("Please insed a number")
numero = int(input())
suma = numero 
while numero >0:
    suma += numero
    print( "su suma es: ", suma)
    if numero < 0: break"""

"""number = 1
while number <=100:
    if number /7 == 1:
        print ("the seveth´s divisible number is: ", number)
        break
    number +=1"""

"""notasMenores = 0
notasMayores = 0
i= 1
while i <= 10:
    nota= float (input (f"please insead the calification {i} :"))
    if nota >= 6:
        notasMayores += 1
    else:
        notasMenores += 1
        i +=1"""


explosion = 10
while explosion > 0:
    explosion -= 1
    print ("the explosion will be to happen in:", explosion, "seconds ")
print ( "END GAME")