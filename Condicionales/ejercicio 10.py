compra = float(input("Ingrese el monto de su compra: "))

if compra > 300000:
    descuento = compra * 0.20
    cantidad_a_pagar = compra - descuento
    print(f"Monto original: ${compra:,.2f}")
    print(f"Descuento (20%): ${descuento:,.2f}")
    print(f"Cantidad a pagar: ${cantidad_a_pagar:,.2f}")
else:
    print(f"Monto original: ${compra:,.2f}")
    print(f"Cantidad a pagar: ${compra:,.2f}")
    print("No aplica descuento (compra menor a $300.000)")
