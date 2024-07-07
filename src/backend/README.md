# Backend

## Resumen

Este subproyecto aloja el backend del proyecto que está desarrollado usando Python, Django y Django Rest Framework.

## Sumario

- [Creación y activación del entorno virtual de python en Windows](#en-windows)
- [Creación y activación del entorno virtual de python en Linux y Mac](#en-linux-y-mac)
- [Ejecutar Proyecto](#ejecutar-proyecto)

## Creación y activación de entorno virtual de python

### En Windows

1. [Descargar Python](https://www.python.org/ftp/python/3.12.4/python-3.12.4-amd64.exe) e instalarlo

2. Reiniciar el equipo, abrir cmd y escribir `py -m pip install virtualenv` y presionar `Enter`

3. Finalizada la instalación escribir `py -m virtualenv -p python3 django` (Reemplace "django" por el nombre que usted desee)

4. Luego activar el entorno virtual colocando `django\Scripts\activate.bat` (Reemplace "django" con el nombre que colocó durante la creación del entorno)

### En Linux y Mac

1. Instalar las versiones developer y gestor pip de python según la distribución de Linux o Mac

    - Para Mac, asegurarse de tener instalado Homebrew, puede instalarlo siguiendo las [instrucciones del sitio oficial](https://brew.sh/)

    - Y luego ejecutar los siguientes comandos

    ```(bash)
    > sudo brew update
    > sudo brew install python3 python3-pip 
    ```

    - Para Linux, dependiendo de la distribución de Linux realizar la instalación de la version developer de python y el gestor de paquetes pip de python, para este ejemplo se asumirá que se utiliza el gestor APT

    ```(bash)
    > sudo apt update
    > sudo apt install python3-dev python3-pip
    ```

2. Luego escribir `pip install virtualenv` y presionar `Enter`

3. Finalizada la instalación escribir `virtualenv -p python3 django` (Reemplace "django" por el nombre que usted desee)

4. Luego activar el entorno virtual colocando `source/django/bin/activate` (Reemplace "django" con el nombre que colocó durante la creación del entorno)

## Ejecutar proyecto

1. Primero se debe seguir las intrucciones de [clonación](../../README.md#clonación-del-proyecto) del proyecto

2. Teniendo activado el [entorno virtual de python](#creación-y-activación-de-entorno-virtual-de-python) dirigise a la carpeta del backend (asumiendo que se encuentra en la carpeta `proyecto_ATW`) escribiendo

    ```(bash)
    (django)> cd src
    (django)src/> cd backend
    (django)src/backend/> 
    ```

3. Luego escribir `pip3 install -r requirements.txt` (esto instalará las dependencias del proyecto backend) en el entorno virtual

4. Para realizar las migraciones escribir `python3 manage.py migrate`

5. Para ejecutar escribir `python3 manage.py 0.0.0.0:8000`
