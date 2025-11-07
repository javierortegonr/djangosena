from django.shortcuts import render
from .models import Saludo # Importamos nuestro Modelo

def mostrar_saludo(request):
    # 1. LÓGICA: Pedir al Modelo (M) el primer saludo que encuentre
    saludo_de_db = Saludo.objects.first() # Obtiene el objeto Saludo que creamos

    # 2. CONTEXTO: Preparar los datos para la Plantilla
    # Creamos un diccionario
    contexto = {
        'saludo_para_template': saludo_de_db
    }

    # 3. RENDER: Enviar la solicitud, la plantilla y los datos
    return render(request, 'saludo.html', contexto)
# Create your views here.

def segunda_vista(request):
    return render(request, 'second.html')

def bio_sena(request):
    """Vista que muestra la biografía completa del SENA"""
    contexto = {
        'titulo': 'SENA - Servicio Nacional de Aprendizaje',
        'fundacion': '21 de junio de 1957',
        'mision': 'Cumplir la función que le corresponde al Estado de invertir en el desarrollo social y técnico de los trabajadores colombianos, ofreciendo y ejecutando formación profesional integral, para la incorporación y el desarrollo de las personas en actividades productivas que contribuyan al desarrollo social, económico y tecnológico del país.',
        'vision': 'En 2030 el SENA será una entidad de clase mundial en formación profesional integral y en el uso y apropiación de tecnología e innovación al servicio de personas y empresas; habrá contribuido decisivamente a incrementar la competitividad de Colombia a través de: Aportes relevantes a la productividad de las empresas.',
    }
    return render(request, 'bio_sena.html', contexto)