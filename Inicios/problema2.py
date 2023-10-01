#Una tienda ofrece un 15% de descuento sobre el total de la compra

#Pedimos el valor del precio de la compra
valor = float(input("Ingrese el valor total de su compra: ").strip())

#Aplicamos el descuento de la compra
descuento = valor * 0.15

#Imprimimos el valor final
valorFinal = valor - descuento
print(f"El valor final de su compra es de: {valorFinal}")