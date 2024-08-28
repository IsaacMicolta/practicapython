print ("Por favor ingrese el valor de su capital:")
capital= float (input("capital"))
print ("ingrese ahora el numero de años que desea ahorrar ese dinero")
t= int (input("time"))
r=12
m = capital*(1+(r/100))**t

print ("La tasa de interes que se tiene en12 cuenta es del 12% anual")
print ("por lo cual su utilidad al finalizar este periodo es quivalente a: $", m)