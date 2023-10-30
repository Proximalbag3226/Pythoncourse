def calcular_precio_total(*args, **kwargs):
    precio_total = sum(args)
    descuento = kwargs.get('descuento', 0)
    impuesto= kwargs.get('impuesto', 0)
    
    precio_total -= (precio_total * descuento)
    precio_total += (precio_total * impuesto)
    
    return precio_total

lista_productos = [100, 65, 30]
dict_opcionales = {
    'descuento': 0.2,
    'impuesto': 0.01
}
    
precio_final = calcular_precio_total(*lista_productos, **dict_opcionales)
print(f"El precio final es de {precio_final}")