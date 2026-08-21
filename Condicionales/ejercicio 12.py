cantidad = int(input("ingrese la cantidad de llantas: "))

if cantidad < 5:
    precio_unitario = 30000
elif 5 <= cantidad <= 10:
    precio_unitario = 25000
else:
    precio_unitario = 20000

total = cantidad * precio_unitario