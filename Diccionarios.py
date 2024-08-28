Productos = {
    "televisor":15.000,
    "celular": 30.000,
    "portatil": 160.000
}

nombres = { "nombre": "carlos", "edad":20, "cursos": ["Python", "Java", "Nodejs"]}
#print (nombres)

"""print (nombres["nombre"])"""

notas_estudiantes ={ 
    "juan": [2.5, 3,4.6],
    "Ana": [3.5, 4.6, 4.9],
    "Luis": [ 4, 2.5, 3.9]
}
"""print (notas_estudiantes)"""

miDiccionario = {
    "nombre": "sara",
    "edad": 30
}

miDiccionario["profesion"] = "intructora"

"""print(miDiccionario)"""


"""miDiccionario = { 
    "nombre": "Sara", "edad": 30, "preofesion": "instructora"
    
    
    }

print (miDiccionario)

del miDiccionario ["profession"]
print(miDiccionario)

proof = miDiccionario.pop ("profesion")
print(proof)
print(miDiccionario)"""

miDiccionario = {"nombre": 
"sara",
"edad": 30,
"profesion": "instructora"
}

nuevosDatos ={
    "ciudad": "cali",
    "documento": 1234567,
    "Telefono" : 22222
}

for clave, valor in nuevosDatos.items():
    miDiccionario[clave] = valor

"""print(miDiccionario)"""