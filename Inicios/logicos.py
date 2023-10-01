#Operadores logicos
#Priodidad de los operadores logicos: 1) Not 2)And 3)Or
a = 10
b = 15
c = 20

#and, este operador compara los dos valors que se le entrgan para asi dar un resultado, en este caso dicho operador es una "multiplicacion" de valores 
#ya que solamente es verdadero si ambos valores son iguales ejemplo: 

resultado1 = ((a<b) and (b<c))
resultado2 = ((a>b) and (b<c))
print(resultado1)
print(resultado2)

#or este operador compara los valores que se le entrgan para asi dar un resultado, en este caso para dicho operador solo es necesario que se tenga un "true"
#en alguno de los dos valors para queel resultado sea verdadero, en caso de tener dos "false" el resultado igual sera falso 

resultado3 = ((a<b) or (b<c))
resultado4 = ((a>b) or (b<c))
print(resultado3)
print(resultado4)

#not la funcion de este operador es retornar lo contrario al valor dado ejemplo  de ello si le entregamos un valor veradero el operador en cuestio
#retornara un valor falso y viceversa

resultado5 = not(resultado2)
resultado6 = not(resultado4)
print(resultado5)
print(resultado6)