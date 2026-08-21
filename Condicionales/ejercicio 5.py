a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))
c = float(input("Ingresa el tercer número: "))

numeros = [a, b, c]
numeros.sort(reverse=True)      

print("numeros ordenados de mayor a menor:")
print(numeros)