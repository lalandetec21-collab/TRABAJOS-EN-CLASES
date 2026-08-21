dia = int(input("ingresar el día: "))
mes = int(input("ingresar el mes: "))
año = int(input("ingresar el año: "))

if año > 0:
    if mes == 2:
        dias_mes = 28
    elif mes in [4, 6, 9, 11]:
        dias_mes = 30
    elif mes in [1, 3, 5, 7, 8, 10, 12]:
        dias_mes = 31
    else:
        dias_mes = 0  

    if 1 <= dia <= dias_mes and dias_mes !=0:
        print("La fecha es correcta.")
    else:
        print("La fecha es incorrecta.")
else:
    print("La fecha es incorrecta.")