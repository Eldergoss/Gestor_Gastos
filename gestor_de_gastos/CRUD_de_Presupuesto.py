import json
import os
from Contabilidad import *

# Crea el expediente (presupuesto, egresos) de gastos
def Crear():
    Expediente_Num = input("Numero de expediente: ")
    Presupuesto = int(input("Presupuesto: "))
    gastos = Egresos() 
    expediente = {Expediente_Num: {"presupuesto": Presupuesto, "gastos": gastos}}
    	
    # Inyección de datos
    with open('base_Gastos.json', "w") as archivo:
    	# Inyecta datos del expediente en el archivo JSON
    	json.dump(expediente, archivo, indent=4)

    return expediente

# Leer datos 
def Leer():
    # Leer datos de un JSON
    with open('base_Gastos.json') as archivo2:
        exp2 = json.load(archivo2)
    
    return exp2

def Editar(expediente):
    # Leer los datos
    with open('base_Gastos.json', "r") as get_data:
        exp3 = json.load(get_data)

    # Edición del valor de presupuesto
    expediente_num = input("Ingrese el número de expediente a editar: ")
    nuevo_presupuesto = int(input("Nuevo Presupuesto: "))
    if expediente_num in expediente:
        expediente[expediente_num]["presupuesto"] = nuevo_presupuesto
    else:
        print("El número de expediente ingresado no existe.")
    
    # funcion de edicion
    expediente = editar_gasto(expediente)




    # Inyectar datos modificados
    with open('base_Gastos.json', "w") as set_data:
        json.dump(exp3, set_data, indent=4)

    #print("Datos del jugador editados.")

    return expediente


def Eliminar():
    expediente_num = input("Ingrese el número de expediente a eliminar: ")
    
    # Verificar si el expediente existe
    if os.path.exists('base_Gastos.json'):
        with open('base_Gastos.json', 'r') as file:
            expedientes = json.load(file)
            
        if expediente_num in expedientes:
            # Eliminar el expediente del diccionario
            del expedientes[expediente_num]
            
            # Escribir los cambios en el archivo JSON
            with open('base_Gastos.json', 'w') as file:
                json.dump(expedientes, file, indent=4)
                
            print(f"Expediente {expediente_num} eliminado exitosamente.")
        else:
            print("El número de expediente ingresado no existe.")
    else:
        print("No hay expedientes para eliminar.")