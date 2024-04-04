from CRUD_de_Presupuesto import *
from Contabilidad import *

# Función para imprimir el menú
def imprimir_menu():
    print("""

  _____                 _      _ 
 |  __ \               (_)    | |
 | |  | |  __ _ __   __ _   __| |
 | |  | | / _` |\ \ / /| | / _` |
 | |__| || (_| | \ V / | || (_| |
 |_____/  \__,_|  \_/  |_| \__,_|
                                 
                                 

***************** Gestor de Gastos *****************
| 1. Crear                                         |
| 2. Leer                                          |
| 3. Editar                                        |
| 4. Borrar                                        |
| 5. Salir                                         |
****************************************************
""")

# Mostrar el menú inicialmente
imprimir_menu()

# Solicitar la selección de opción al usuario
opcion = input("Seleccione una opción: ")

# Ejecutar la opción seleccionada
if opcion == "1":
    print("Creando nuevo expediente")
    expediente = Crear()
    print(f"Expediente creado: {expediente}")

elif opcion == "2":
    print("Leyendo datos del expediente...")
    expediente = Leer()
    print(f"Datos del expediente leído: {expediente}")

if opcion == "3":
    print("Edición de datos del expediente")
    expediente = Leer()
    edicion_expediente = Editar(expediente)
    print(f"Datos del expediente han sido modificados: {edicion_expediente}")


elif opcion == "4":
    print("Eliminando expediente...")
    Eliminar()

elif opcion == "5":
    print("Saliendo del programa...")
else:
    print("Opción no válida. Por favor, seleccione una opción válida.")