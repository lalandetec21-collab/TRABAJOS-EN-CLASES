a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))

if b == 0:
    print("No se puede comprobar si un número es múltiplo de cero.")
elif a % b == 0:
    print("El primer número es múltiplo del segundo.")
elif b % a == 0:
    print("El segundo número es múltiplo del primero.")
else:
    print("Ninguno de los números es múltiplo del otro.")