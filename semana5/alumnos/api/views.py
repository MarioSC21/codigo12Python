from django.http import JsonResponse

#?framework rest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AlumnoSerialixer

from .models import Alumno

def index(requesty):
    return JsonResponse({
        'mensaje':'Bienvenido a mi Api'
    })

@api_view(['GET'])    
def home(request):
    return Response({
        'status':'ok',
        'message':'hola mundo desde rest'
    })

def alumnos(request):
    dataAlumnos = Alumno.objects.all() #traigo todos los alumnos en forma de objetos
    listaAlumnos = []
    for alumno in dataAlumnos:
        dicAlumno = {
            'nombre': alumno.nombre,
            'email': alumno.email
        }
        listaAlumnos.append(dicAlumno)
    
    context = {
        'status':'ok',
        'data': listaAlumnos
    }
    return JsonResponse(context)

#serializer
@api_view(['GET'])
def getAlumnos(request):
    listaAlumnos = Alumno.objects.all()
    serAlumnos = AlumnoSerialixer(listaAlumnos,many=True)
    
    context = {
        'status':'ok',
        'data': serAlumnos.data
    }
    return Response(context)

@api_view(['POST'])
def setAlumno(request):
    serAlumno = AlumnoSerialixer(data=request.data)
    serAlumno.is_valid(raise_exception=True)

    nuevoAlumno = serAlumno.save()

    context = {
        'status':'ok',
        'message':'alumno creado',
        'data':AlumnoSerialixer(nuevoAlumno).data
    }

    return Response(context)

######### ENDPOINTS PROFESOR
from .models import Profesor
from .serializers import ProfesorSerializer

@api_view(['GET','POST'])
def profesor(request):
    if request.method == 'GET':
        lstProfesores = Profesor.objects.all()
        serProfesores = ProfesorSerializer(lstProfesores,many=True)
        
        return Response(serProfesores.data)

    elif request.method == 'POST':
        serProfesor = ProfesorSerializer(data=request.data)
        if serProfesor.is_valid():
            serProfesor.save()
            return Response(serProfesor.data)
        else:
            return Response(serProfesor.errors)

@api_view(['GET','PUT','DELETE'])
def profesor_detail(request,profesor_id):
    objProfesor = Profesor.objects.get(id=profesor_id)

    if request.method == 'GET':
        serProfesor = ProfesorSerializer(objProfesor)
        return Response(serProfesor.data)

    elif request.method=='PUT':
        serProfesor = ProfesorSerializer(objProfesor,data=request.data)
        if serProfesor.is_valid():
            serProfesor.save()
            return Response(serProfesor.data)
        else:
            return Response(serProfesor.errors)
    elif request.method == 'DELETE':
        objProfesor.delete()
        return Response(status=204)