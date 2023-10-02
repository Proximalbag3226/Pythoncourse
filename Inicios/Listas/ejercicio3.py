#Escriba un programa donde se cree una lista con los siguientes personajes del señor de los anillos
#Nombre: Aragorn, clase: guerrero, raza: dunadan del norte
#Nombre: Gandalf, clase: mago, raza: Istar
#Nombre: Legolas, clase: arquero, raza: elfo sindar 

#Creamos una lista vacia 
personajes = []

#Agregamos al primer personaje 
p = {"Nombre":"Aragonr", "Clase":"Guerrero", "Raza":"Dunadan del norte"}

#Agragamos al personaje a la lista vacia
personajes.append(p)

#Continuacmos con el segundo
p = {"Nombre":"Gandalf", "Clase":"Mago", "Raza":"Istar"}
personajes.append(p)

#Y con el tecero
p = {"Nombre":"Legolas", "Clase":"Arquero", "Raza":"Elfo"}
personajes.append(p)

#Imprimimos la lista de los personajes
print(personajes)