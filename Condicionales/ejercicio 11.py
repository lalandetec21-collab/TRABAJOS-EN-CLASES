numero = int(input("Ingresa un número de tres cifras: "))

if 100 <= numero <= 999:
    centenas = numero // 100
    decenas = (numero // 10) % 10
    unidades = numero % 10

    if unidades == centenas:
        print("El número es capicúa.")
    else:
        print("El número no es capicúa.")
else:
    print("El número debe tener tres cifras.")