from django.shortcuts import render,redirect
from .models import Curso,Docente,Especialidad
# Create your views here.

#cursos
def Cursos(request):
    cursosListado=Curso.objects.all()
    return render(request,"GestionCursos.html",{"cursos":cursosListado})

def registrarcurso(request):
    codigo=request.POST["txtcodigo"]
    nombre=request.POST["txtnombre"]
    creditos=request.POST["numcreditos"]

    curso=Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    return redirect('/curso')

def eliminarcurso(request,codigo):
    curso=Curso.objects.get(codigo=codigo)
    curso.delete()
    return redirect('/curso')


def Docentes(request):
    docentesListado=Docente.objects.all()
    return render(request,"GestionDocentes.html",{"docentes":docentesListado})

def registrardocente(request):
    IdDocente=request.POST["txtIdDocente"]
    Nombre=request.POST["txtNombre"]
    Apellido=request.POST["txtApellido"]
    FIngreso=request.POST["dateFIngreso"]
    Dni=request.POST["txtDni"]
    Telefono=request.POST["numTelefono"]

    docente=Docente.objects.create(IdDocente=IdDocente, Nombre=Nombre, Apellido=Apellido, FIngreso=FIngreso,Dni=Dni, Telefono=Telefono)
    return redirect('/docente')