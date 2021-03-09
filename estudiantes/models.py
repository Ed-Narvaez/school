# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from six import python_2_unicode_compatible

@python_2_unicode_compatible
class Evaluacion(models.Model):
    titulo = models.CharField(max_length=100, verbose_name=u'Título', unique=True)
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.titulo
@python_2_unicode_compatible
class Notas(models.Model):
    evaluacion = models.ForeignKey(Evaluaciones.objects.all(),on_delete=models.CASCADE)
    nota = models.TextField(verbose_name=u'Nota', help_text=u'Nota del estudiante')
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
@python_2_unicode_compatible
class Asistencia(models.Model):
    dia = models.CharField(max_length=100, verbose_name=u'Dia', unique=True)
    asistio = models.TextField(verbose_name=u'Nota', help_text=u'Asistio a clases')
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
@python_2_unicode_compatible
class Registrar(models.Model):
    evaluacion = models.ForeignKey(Evaluaciones.objects.all(),on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
