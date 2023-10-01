#Hacer un programa que simule un cajero automatico con saldo inicial de 1000$ y que tenga las opciones de retirar dinero, depositar. mostrar saldo y salir

saldo = 1000

def retirar(saldo):
    retiro = int(input("Ingrese la cantidad a retirar ").strip())
    if retiro>saldo:
        print("Usted no cuenta con los fondos sufientes")       
    else:
        saldo -= retiro
        print(f"Su retiro de {retiro} se completo con exito, su nuevo saldo es de {saldo}.")
        return saldo

def depositar(saldo):
    deposito = int(input("Ingrese la cantidad a depositar ").strip())
    saldo += deposito
    print(f"Su deposito de {deposito} se completo con exito, su nuevo saldo es de {saldo}.")
    return saldo        

def consulta(saldo):
    print(saldo)

def cajero():
    print("Bienvenido al cajero automatico, selecciona la operacion a realizar")
    while True:
        print("1.- Retiro")
        print("2.- Deposito")
        print("3.- Consulta de saldo")
        print("4.- Salir")

        operacion = input("Eligue la operacion a relizar ").strip()
        if operacion == "1":
            retirar(saldo)      

        elif operacion == "2":
            depositar(saldo)
    
        elif operacion == "3":
            consulta(saldo)

        elif operacion == "4":
            break
cajero()


