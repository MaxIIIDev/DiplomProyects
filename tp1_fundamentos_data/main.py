import os
def menu():
    print("=== Sistema de Datos Personales")
    print("1 - Calcular IMC")
    print("2 - Precio de entrada")
    print("3 - Analizar texto")
    print("4 - Simulador de ingresos mensuales")
    print("5 - Salir")
def limpiar_consola():
    os.system("cls")
def main():
    execute = True
    while execute:
        limpiar_consola()
        menu()
        print("Digite su opcion")
        opcion = int(opcion) if (opcion:= input("=> ")).isdigit() else 0
        match opcion:
            case 1:
                limpiar_consola()
                peso = float(peso) if  (peso:= input( "Ingrese su peso= ")).replace(".", "").isdigit() else -1
                while peso < 0 or peso > 300:
                    limpiar_consola()
                    print("Ingrese un peso valido")
                    peso = float(peso) if  (peso:= input("Ingrese su peso= ")).replace(".", "").isdigit() else -1

                altura = float(altura) if  (altura:=input( "Ingrese su altura= ")).replace(".", "").isdigit() else -1
                while altura < 0 or altura > 2.50:
                    limpiar_consola()
                    print("Ingrese una altura valido")
                    
                    altura = float(altura) if  (altura:=input( "Ingrese su altura= ")).replace(".", "").isdigit() else -1
                    
                imc = peso / (altura **2)
                if imc > 25:
                    limpiar_consola()
                    print(f"Su IMC es: {imc:.2f}")
                    print("Atencion, su IMC es muy alto")
                    input("Presione enter para volver al menu= ")
            case 2:
                print("ingreso")
            case 3:
                print("Ingrese su texto")
            case 4:
                print("Ingrese su ingreso")
            case 5:
                execute = False
                limpiar_consola()
                print("Gracias por usar el sistema")
                input("Presione enter para salir")
            case _:
                print("Opcion invalida")
                input("Presione enter para volver al menu")
        
        limpiar_consola()
        
main()