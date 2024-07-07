# Establecemos una imagen de python con la versión que necesitemos
FROM python:3.11

# ENV PYTHONUNBUFFERED 1 establece una variable de entorno que permite
# enviar el log de django directamente al log del contenedor
ENV PYTHONUNBUFFERED 1 

# Indicamos donde (dentro del contenedor) vamos a trabajar
WORKDIR /app

# Indicamos a docker que copie el archivo indicado en la carpeta dentro
# dentro del contenedor
ADD ./requirements.txt /app/

# Ejecutamos el la instalación de los paquetes del archivo indicado
RUN pip3 install --no-cache-dir -r requirements.txt

# Una nez instalados los paquetes procedemos a copiar el resto en el contenedor
ADD . /app/

# Ejecutamos el comando para migrar la bd a sqlite
RUN python manage.py migrate

# Exponemos el puerto 8000 para que podamos acceder desdeel host
EXPOSE 8000/tcp

# Ejecutamos el comando para iniciar el servidor de desarrollo de django 
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]