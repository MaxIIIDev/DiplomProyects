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
        opcion_seleccionada = int(opcion_seleccionada) if (opcion_seleccionada:= input("=> ")).isdigit() else 0
        match opcion_seleccionada:
            case 1: #Calcular IMC
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
            case 2: #Precio de entrada
                limpiar_consola()
                edad = int(edad) if  (edad:= input( "Ingrese su edad= ")).isdigit() else -1
                
                while edad < 0 or edad > 120:
                    limpiar_consola()
                    print("Ingrese una edad valido")
                    edad = int(edad) if  (edad:= input( "Ingrese su edad= ")).isdigit() else -1
                if( edad < 4):
                    limpiar_consola()
                    print("Categoria asignada: Infantil | Precio: 0")
                    input("Presione enter para volver al menu= ")
                elif(edad > 12 and edad < 18):
                    limpiar_consola()
                    print("Categoria asignada: Junior | Precio: 400")
                    input("Presione enter para volver al menu= ")
                else: 
                    limpiar_consola()
                    print("Categoria asignada: Adulto | Precio: 800")
                    input("Presione enter para volver al menu= ")
            case 3: #Analizar texto
                limpiar_consola()
                print("Ingrese su texto")
                texto_ingresado = input("Ingrese su texto= ")
                print("Su texto analizado:")
                print(f"Su texto en mayusculas: {texto_ingresado.upper()}")
                print(f"La cantidad de caracteres: {len(texto_ingresado)}")
                print(f"La cantidad de veces que aparece la palabra 'Python': {texto_ingresado.lower().count('python')}")
                print(f"Su texto invertido: {texto_ingresado[::-1]}")
                input("Presione enter para volver al menu= ")
            case 4: #Simulador de ingresos mensuales
                meses_a_analizar = int(meses_a_analizar) if  (meses_a_analizar:= input( "Ingrese el numero de meses a analizar= ")).isdigit() else -1
                while meses_a_analizar < 0:
                    limpiar_consola()
                    print("Ingrese un numero valido")
                    meses_a_analizar = int(meses_a_analizar) if  (meses_a_analizar:= input( "Ingrese el numero de meses a analizar= ")).isdigit() else -1
                total_acumulado = 0
                numero_mayor = 0
                numero_menor = 0
                
                for i in range(meses_a_analizar):
                    limpiar_consola()
                    print(f"Ingrese el importe del ingreso del mes {i+1}")
                    importe_ingreso = int(importe_ingreso) if  (importe_ingreso:= input( "Ingrese el importe del ingreso del mes= ")).isdigit() else -1
                    while importe_ingreso < 0:
                        limpiar_consola()
                        print("Ingrese un importe valido")
                        importe_ingreso = int(importe_ingreso) if  (importe_ingreso:= input( "Ingrese el importe del ingreso del mes= ")).isdigit() else -1
                    else:
                        if(i == 0):
                            numero_mayor = importe_ingreso
                            numero_menor = importe_ingreso
                        total_acumulado += importe_ingreso
                        if importe_ingreso >= numero_mayor:
                            numero_mayor = importe_ingreso
                        if importe_ingreso <= numero_menor:
                            numero_menor = importe_ingreso
                limpiar_consola()
                print(f"El total acumulado de ingresos es: {total_acumulado}")
                print(f"El mayor ingreso fue: {numero_mayor}")
                print(f"El menor ingreso fue: {numero_menor}")
                input("Presione enter para volver al menu= ")
                    
            case 5: #Salir
                execute = False
                limpiar_consola()
                print("Gracias por usar el sistema")
                input("Presione enter para salir")
            case _: #Opcion invalida
                print("Opcion invalida")
                input("Presione enter para volver al menu")
        
        limpiar_consola()
        
main()