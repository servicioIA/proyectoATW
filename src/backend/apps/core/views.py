from django.shortcuts import render, redirect
from apps.core.models import Persona
import csv
from django.contrib import messages
from .models import Pregunta
from .forms import CargarArchivoForm
from .models import Conversacion


def index(request):
    template_name = "index.html"
    context = {} 
    return render(request, template_name, context)


def importar_preguntas(request):
    if request.method == 'POST':
        form = CargarArchivoForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = request.FILES['archivo']
            if archivo.name.endswith('.csv'):
                reader = csv.reader(archivo.read().decode('utf-8').splitlines())
                for row in reader:
                    Pregunta.objects.create(
                        texto=row[0],
                        categoria=row[1],
                        dificultad=row[2]
                    )
                messages.success(request, 'Preguntas importadas con éxito')
                return redirect('importar_preguntas')
            else:
                messages.error(request, 'Por favor suba un archivo CSV')
    else:
        form = CargarArchivoForm()
    return render(request, 'importar_preguntas.html', {'form': form})

import csv
from .models import DatosEntrenamiento
from .forms import CargarArchivoEntrenamientoForm
from .utils import entrenar_modelo

def importar_datos_entrenamiento(request):
    if request.method == 'POST':
        form = CargarArchivoEntrenamientoForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = request.FILES['archivo']
            if archivo.name.endswith('.csv'):
                reader = csv.reader(archivo.read().decode('utf-8').splitlines())
                for row in reader:
                    DatosEntrenamiento.objects.create(
                        pregunta=row[0],
                        respuesta=row[1]
                    )
                messages.success(request, 'Datos de entrenamiento importados con éxito')
                entrenar_modelo()
                return redirect('importar_datos_entrenamiento')
            else:
                messages.error(request, 'Por favor suba un archivo CSV')
    else:
        form = CargarArchivoEntrenamientoForm()
    return render(request, 'importar_datos_entrenamiento.html', {'form': form})



def chat(request):
    if request.method == 'POST':
        mensaje_usuario = request.POST.get('mensaje')
        # Aquí llamas a tu modelo de chatbot para obtener la respuesta
        respuesta_bot = obtener_respuesta_chatbot(mensaje_usuario)

        # Guardar la conversación en la base de datos (opcional)
        if request.user.is_authenticated:
            Conversacion.objects.create(
                usuario=request.user,
                mensaje=mensaje_usuario,
                respuesta=respuesta_bot
            )

        # Almacenar la conversación en la sesión
        if 'conversacion' not in request.session:
            request.session['conversacion'] = []
        request.session['conversacion'].append({
            'mensaje': mensaje_usuario,
            'respuesta': respuesta_bot
        })

        return redirect('chat')

    conversacion = request.session.get('conversacion', [])
    return render(request, 'chat.html', {'conversacion': conversacion})

def reiniciar_conversacion(request):
    if 'conversacion' in request.session:
        del request.session['conversacion']
    messages.success(request, 'La conversación ha sido reiniciada.')
    return redirect('chat')

def obtener_respuesta_chatbot(mensaje):
    # Aquí va la lógica para obtener la respuesta del chatbot
    # Esto es solo un ejemplo
    return "Esta es una respuesta del chatbot"
