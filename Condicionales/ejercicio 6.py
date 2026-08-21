dia = int(input("ingresar el dia: "))
mes = int(input("ingresar el mes: "))
año = int(input("ingresar el año: "))

if 1 <= dia <= 30 and 1 <= mes <= 12 and año > 0:
    print("La fecha es correcta.")
else:
    print("La fecha es incorrecta.")