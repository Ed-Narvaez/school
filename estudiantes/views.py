# coding:utf-8

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.core.mail import EmailMessage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactoForm, EvaluacionForm, NotasForm, AsistenciaForm
from .models import Evaluacion, Notas, Asistencia, Registrar


@login_required(login_url='/ingresar')
def cerrar(request):
    logout(request)
    return HttpResponseRedirect('/')

def contacto(request):
    if request.method=='POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            titulo = 'Mensaje desde el recetario de Maestros del Web'
            contenido = formulario.cleaned_data['mensaje'] + "\n"
            contenido += 'Comunicarse a: ' + formulario.cleaned_data['correo']
            correo = EmailMessage(titulo, contenido, to=['destinatario@email.com'])
            try:
                correo.send()
            except Exception as e:
                print('No fue posible enviar el mensaje, revisar la configuración')
                print(e)
            return HttpResponseRedirect('/')
    else:
        formulario = ContactoForm()
    context = {'formulario': formulario}
    return render(request, 'contactoform.html',context)

def inicio(request):
    evaluacion = Evaluacion.objects.all()
    context = {'estudiantes': evaluacion}
    return render(request, 'inicio.html', context)

def ingresar(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/privado')
    if request.method == 'POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)

                    if usuario == "profesor":
                        return HttpResponseRedirect('/profesor')
                    else:
                        return HttpResponseRedirect('/estudiante')
                else:
                    return render(request, 'noactivo.html')
            else:
                return render(request, 'nousuario.html')
    else:
        formulario = AuthenticationForm()
    context = {'formulario': formulario}
    return render(request, 'ingresar.html', context)

@login_required(login_url='/ingresar')
def privado(request):
    usuario = request.user
    context = {'usuario': usuario}
    return render(request, 'privado.html', context)

def evaluacion_nueva(request):
    if request.method=='POST':
        formulario = EvaluacionForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/profesor')
    else:
        formulario = RecetaForm()
    context = {'formulario': formulario}
    return render(request, 'evaluacionform.html', context)
def calificar(request):
    if request.method=='POST':
        formulario = NotasForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/profesor')
    else:
        formulario = RecetaForm()
    context = {'formulario': formulario}
    return render(request, 'notasform.html', context)
def asistencia(request):
    if request.method=='POST':
        formulario = AsistenciaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/profesor')
    else:
        formulario = RecetaForm()
    context = {'formulario': formulario}
    return render(request, 'asistenciaform.html', context)
def registrar(request):
    if request.method=='POST':
        formulario = RegistrarForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/estudiante')
    else:
        formulario = RecetaForm()
    context = {'formulario': formulario}
    return render(request, 'registrarform.html', context)

def evaluaciones(request):
    notas = Notas.objects.all()
    asistencia = Asistencia.objects.all()
    evaluaciones = Evaluacion.objects.all()
    context = {'notas': notas,'evaluaciones': evaluaciones,'asistencias': asistencia}
    return render(request, 'usuariosnotas_user.html', context)
def notas(request):
    notas = Notas.objects.all()
    asistencia = Asistencia.objects.all()
    evaluaciones = Evaluacion.objects.all()
    context = {'notas': notas,'evaluaciones': evaluaciones,'asistencias': asistencia}
    return render(request, 'notas.html', context)

def usuarios(request):
    usuarios = User.objects.all()
    evaluacion = Evaluacion.objects.all()
    context = {'estudiantes': evaluacion, 'usuarios':usuarios}
    return render(request, 'evaluaciones_user.html', context)

def usuario_nuevo(request):
    if request.method=='POST':
        formulario = UserCreationForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserCreationForm()
    context = {'formulario': formulario}
    return render(request, 'nuevousuario.html', context)

def sobre(request):
    html = "<html><body>Proyecto para el manejo de las notas de estudiantes</body></html>"
    return HttpResponse(html)
