# Proyecto ejemplo para Aplicaciones y Tecnologías Web

## Resumen

Este proyecto ha sido creado con la finalidad de presentar un ejemplo de ejecución de un proyecto web con una arquitectura básica de cliente servidor utilizando las tencologías Angular para el frontend y Django con Django Rest Framework para el backend

## Sumario

* Clonación del proyecto

* [Instructivo de ejecución del Docker Compose](#ejecución-en-docker-compose)

* [Instructivo de ejecución del Frontend](src/frontend/README.md)

* [Instructivo de ejecución del Backend](src/backend/README.md)

## Clonación del proyecto

1. Buscar un directorio en el equipo, abrir cmd o Powershell y escribir lo siguiente:
`git clone https://github.com/rodoaravena/proyecto_ATW.git`

    Ejemplo:

    ```(bash)
    C:\Users\estudiante\directorio\en\el\equipo> git clone https://github.com/rodoaravena/proyecto_ATW.git    
    ```

2. Finalizada la clonación escribir `cd proyecto_ATW` para ingresar la carpeta y presionar `Enter`

3. Luego realizar los pasos de ejecución en [Docker](#ejecución-en-docker-compose) o por separado el [Frontend](src/frontend/README.md) y [Backend](src/backend/README.md#ejecutar-proyecto)

## Ejecución en Docker Compose

**Nota:** Si se utiliza esta opción no realizar las intrucciones para el frontend y el backend.

1. Instalar Docker, seguir estas instrucciones según el Sistema Operativo a utilizar:
    * [Instrucciones de instalación para Windows](https://docs.docker.com/desktop/install/windows-install/)
    * [Instrucciones de instalación para Linux](https://docs.docker.com/desktop/install/linux-install/)
    * [Instrucciones de instalación para Mac](https://docs.docker.com/desktop/install/mac-install/)

2. Luego, escribir el siguiente comando `docker compose build --no-cache` y presionar `Enter`

3. Finalizada la construcción de las imagenes escribir el siguiente `docker compose up` y presionar `Enter`

4. Si todo funciona a la perfección, docker ejecutará los contenedores y sólo debería abrir el navegador e ingresar a `http://localhost:4200` para ver el frontend y a `http://localhost:8000/admin` para ver el administrador de django en el backend
