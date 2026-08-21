numeros_texto = {
    0: "cero",
    1: "uno",
    2: "dos",
    3: "tres",
    4: "cuatro",
    5: "cinco",
    6: "seis",
    7: "siete",
    8: "ocho",
    9: "nueve",
    10: "diez"
}

while True:
    try:
        nota = int(input("Ingrese una nota entre 0 y 10: "))
        if 0 <= nota <= 10:
            print(f"La nota es: {numeros_texto[nota]}")
            break
        else:
            print("Error: La nota debe estar entre 0 y 10")
    except ValueError:
        print("Error: Debe ingresar un número entero")
