django-admin startproject myproject

cd myproject
python manage.py startapp director

from django.db import models

class Director(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

class Pelicula(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo
      
from django.shortcuts import render
from .models import Director

def lista_directores(request):
    directores = Director.objects.all()
    return render(request, 'lista_directores.html', {'directores': directores})

def peliculas_director(request, director_id):
    director = Director.objects.get(pk=director_id)
    peliculas = director.pelicula_set.all()
    return render(request, 'peliculas_director.html', {'director': director, 'peliculas': peliculas})

  {% extends 'base.html' %}

{% block content %}
<h1>Directores</h1>
<ul>
  {% for director in directores %}
  <li><a href="{% url 'peliculas_director' director.id %}">{{ director.nombre }}</a></li>
  {% endfor %}
</ul>
{% endblock %}

{% extends 'base.html' %}

{% block content %}
<h1>{{ director.nombre }}</h1>
<ul>
  {% for pelicula in peliculas %}
  <li><h2>{{ pelicula.titulo }}</h2><p>{{ pelicula.descripcion }}</p></li>
  {% endfor %}
</ul>
{% endblock %}

from django.contrib import admin
from .models import Director, Pelicula

admin.site.register(Director)
admin.site.register(Pelicula
