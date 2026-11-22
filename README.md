# Sistema Integral de Gestión de Clientes, Servicios y Reservas – Software FJ

## 1. Descripción del proyecto

Este proyecto consiste en el desarrollo de un sistema integral para la gestión de clientes, servicios y reservas de la empresa Software FJ. La aplicación fue desarrollada en Python utilizando el paradigma de Programación Orientada a Objetos (POO).

El sistema permite registrar clientes, administrar diferentes tipos de servicios, crear y gestionar reservas, controlar errores durante la ejecución y almacenar un registro de los eventos realizados.

## 2. Objetivo

Implementar una aplicación orientada a objetos que permita gestionar clientes, servicios y reservas, aplicando mecanismos de manejo de excepciones para mejorar la estabilidad y robustez del sistema.

## 3. Estructura del proyecto

El proyecto está organizado en los siguientes archivos:

- **main.py:** contiene la ejecución principal del sistema y las pruebas de funcionamiento.
- **entidades.py:** define la clase abstracta Entidad.
- **clientes.py:** contiene la clase Cliente y sus validaciones.
- **servicios.py:** define los servicios disponibles y sus métodos de cálculo y validación.
- **reservas.py:** administra la creación, confirmación, procesamiento y cancelación de reservas.
- **excepciones.py:** contiene las excepciones personalizadas del sistema.
- **logs.txt:** almacena los eventos, advertencias y errores generados durante la ejecución.

## 4. Funcionalidades implementadas

- Registro y validación de clientes.
- Administración de diferentes tipos de servicios.
- Creación y gestión de reservas.
- Cálculo del costo de los servicios.
- Confirmación y cancelación de reservas.
- Manejo de excepciones personalizadas.
- Registro de eventos y errores en un archivo de texto.
- Ejecución de pruebas para comprobar el funcionamiento del sistema.

## 5. Tecnologías utilizadas

- Lenguaje de programación: Python.
- Entorno de desarrollo: Visual Studio Code.
- Control de versiones y almacenamiento: Git y GitHub.

## 6. Ejecución del proyecto

Para ejecutar el sistema, se debe abrir la carpeta del proyecto en Visual Studio Code y ejecutar el siguiente comando desde la terminal:

```bash
python main.py
```

El sistema mostrará los resultados de las operaciones realizadas y registrará los eventos y errores en el archivo `logs.txt`.

## 7. Autor

Brayan Rojas

Programa: Ingeniería de Sistemas

Universidad Nacional Abierta y a Distancia – UNAD
