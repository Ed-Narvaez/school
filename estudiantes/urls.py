from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.inicio, name='inicio'),
    url(r'^cerrar/$', views.cerrar, name='cerrar'),
    url(r'^profesor/$', views.evaluaciones, name='profesor'),
    url(r'^estudiante/$', views.notas, name='estudiante'),
    url(r'^contacto/$', views.contacto, name='contacto'),
    url(r'^ingresar/$', views.ingresar, name='ingresar'),
    url(r'^privado', views.privado, name='privado'),
    url(r'^evaluaciones/$', views.evaluaciones, name='evaluaciones'),
    url(r'^notas/$', views.notas, name='notas'),
    url(r'^evaluacion/nueva/$', views.evaluacion_nueva, name='evaluacion_nueva'),
    url(r'^usuarios/$', views.usuarios, name='usuarios'),
    url(r'^usuario/nuevo/$', views.usuario_nuevo, name='usuario_nuevo'),
    url(r'^sobre/$', views.sobre, name='sobre'),
    url(r'^calificar/$', views.calificar, name='calificar'),
    url(r'^registrar/evaluacion/$', views.registrar, name='registrar'),
    url(r'^asistencia/$', views.asistencia, name='asistencia'),
]
