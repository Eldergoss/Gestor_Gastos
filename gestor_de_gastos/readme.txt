# Gestor de Gastos

Este programa proporciona un sistema para administrar los gastos mediante la creación, lectura, edición y eliminación de expedientes de gastos.

## Funciones Principales

### Crear

La función `Crear()` permite al usuario ingresar un número de expediente, un presupuesto y los gastos asociados. Luego, crea un archivo JSON llamado `base_Gastos.json` para almacenar la información del expediente.

### Leer

La función `Leer()` lee los datos almacenados en el archivo JSON `base_Gastos.json` y muestra los detalles del expediente de gastos.

### Editar

La función `Editar()` permite al usuario editar el presupuesto y los gastos de un expediente específico. Los cambios se guardan en el archivo JSON `base_Gastos.json`.

### Eliminar

La función `Eliminar()` permite al usuario eliminar un expediente de gastos. El expediente se elimina del archivo JSON `base_Gastos.json`.

## Uso del Programa

Al ejecutar el programa, se muestra un menú con las opciones disponibles. El usuario puede seleccionar una opción ingresando el número correspondiente.

## Requisitos

El programa utiliza el módulo `json` de Python para manejar archivos JSON. Además, se requiere el módulo `Contabilidad` que contiene las funciones relacionadas con la gestión de gastos.

## Autor

Este programa fue creado por [Jose david].

