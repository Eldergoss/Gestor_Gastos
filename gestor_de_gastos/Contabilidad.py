"""# Revisado por GPT: La función Egresos se encarga de solicitar al usuario los gastos ingresados.
def Egresos():
    # Inicializa una lista vacía para almacenar los gastos ingresados por el usuario
    gastos = []
    
    # Ciclo while que se ejecuta hasta que el usuario decida salir
    while True:
        # Solicita al usuario que ingrese un gasto
        egreso = int(input("Ingresa los Gastos: "))
        
        # Agrega el gasto a la lista de gastos
        gastos.append(egreso)
        
        # Pregunta al usuario si desea agregar más gastos
        exit = input("¿Quieres agregar más gastos? (s/n): ")
        
        # Si el usuario no desea agregar más gastos, termina el ciclo
        if exit.lower() == "n":
            break
    
    # Retorna la lista de gastos
    return gastos

# Revisado por GPT: La función Modlist se encarga de editar la lista recibida como argumento.
def Modlist(lista):
    print("Lista actual:", lista)
    respuesta = input("¿Desea cambiar algún elemento de la lista? (s/n): ")
    
    if respuesta.lower() == "s":
        indice = int(input("Ingrese el índice del elemento a modificar: "))
        
        # Verificamos si el índice está dentro del rango de la lista
        if indice >= 0 and indice < len(lista):
            nuevo_valor = input("Ingrese el nuevo valor para el elemento: ")
            lista[indice] = nuevo_valor
            print("Elemento modificado correctamente.")
        else:
            print("Índice fuera de rango. No se pudo modificar el elemento.")
    
    return lista

"""
from CRUD_de_Presupuesto import *
 

# Revisado por GPT: La función Egresos se encarga de solicitar al usuario los gastos ingresados.
def Egresos():
    # Inicializa un diccionario vacío para almacenar los gastos ingresados por el usuario
    gastos = {}
    
    # Ciclo while que se ejecuta hasta que el usuario decida salir
    while True:
        # Solicita al usuario que ingrese un gasto y su descripción
        descripcion = input("Ingresa la descripción del gasto: ")
        egreso = int(input("Ingresa el monto del gasto: "))
        
        # Agrega el gasto al diccionario de gastos con su descripción como clave
        gastos[descripcion] = egreso
        
        # Pregunta al usuario si desea agregar más gastos
        exit = input("¿Quieres agregar más gastos? (s/n): ")
        
        # Si el usuario no desea agregar más gastos, termina el ciclo
        if exit.lower() == "n":
            break
    
    # Retorna el diccionario de gastos
    return gastos

def editar_gasto(expediente):
    expediente_num = input("Ingrese el número de expediente: ")
    while True:
        gasto_a_editar = input("Ingrese el nombre del gasto a editar (o 'fin' para terminar): ")
        if gasto_a_editar == "fin":
            break
        if gasto_a_editar in expediente.get(expediente_num, {}).get("gastos", {}):
            nuevo_valor = int(input(f"Ingrese el nuevo valor para '{gasto_a_editar}': "))
            expediente[expediente_num]["gastos"][gasto_a_editar] = nuevo_valor
        else:
            print("El gasto ingresado no existe en los gastos actuales.")
    return expediente




