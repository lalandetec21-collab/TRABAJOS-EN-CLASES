dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))

dia += 1 

if dia > 30:
    dia = 1
    mes += 1
    
    if mes > 12:
        mes = 1
        año += 1

print(f"La fecha del día siguiente es: {dia}/{mes}/{año}")
