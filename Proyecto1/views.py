from pipes import Template
from django.http import HttpResponse
from django.template import Template, Context
import datetime

def saludo(request):
    return HttpResponse ("Yo Era una Aikos")
def segunda_vista(request):
    return HttpResponse ("Y estaba haciendo mis cosas de Aiko")
def diaDeHoy(request):
    dia = datetime.datetime.now()
    
    texto = f"Hoy es dia  {dia}"
    return HttpResponse(texto)
def miNombre(request, nombre):
    
    texto = f"Mi nombres es{nombre}"
    return HttpResponse (texto)
def edad (self, edad):
    edad2 = int(edad)
    
    anio = datetime.datetime.today().year
    
    anio2 =int(anio)
    
    nacimiento = anio2-edad2
    
    docDeText = f'Usted nacio en el año {nacimiento}'
    
    return HttpResponse(docDeText)

def probandoTemplate(request):
    
     miHtml = open('D:/Proyecto1/Plantillas/maquina1.html', )
     
     plantilla = Template(miHtml.read())
     
     miHtml.close()
     
     miContexto = Context()
     
     documento = plantilla.render(miContexto)
     
     return HttpResponse(documento)