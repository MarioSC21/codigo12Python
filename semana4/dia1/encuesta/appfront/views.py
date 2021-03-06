from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def app_index(request):
    titulo = 'Encuesta a alumnos'
    context = {
        'titulo':titulo
    }
    return render(request,'index.html',context)

def detalle(request,pregunta_id):
    return HttpResponse('pregunta nro %s.' % pregunta_id)

def enviar(request):
    context = {
        'titulo':'RESULTADO DE LA ENCUESTA',
        'nombre': request.POST['nombre'],
        'rol': request.POST['rol'],
        'idiomas': request.POST.getlist('idiomas')
    }

    return render(request,'respuesta.html',context)