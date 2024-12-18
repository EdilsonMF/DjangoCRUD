from django.db import models
from django.contrib.auth.models import User

# Modelo para las tareas
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False)
    borrador = models.BooleanField(default=False)
    publicado = models.BooleanField(default=False)
    comentarios = models.TextField(blank=True)

    # Relación con Author y Category
    author = models.ForeignKey('Author', null=True, blank=True, on_delete=models.SET_NULL)  # Relación con Author
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)  # Relación con Category
    
    # Relación con el usuario que crea la tarea
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' - by ' + self.user.username

# Modelo para los autores
class Author(models.Model):
    name = models.CharField(max_length=30)
    profesion = models.TextField(blank=True)
    edad = models.IntegerField(null=False, blank=False)  # Campo obligatorio

    def __str__(self):
        return self.name

# Modelo para las categorías
class Category(models.Model):
    categoria = models.CharField(max_length=100, blank=True) 
    subcategoria=models.CharField(max_length=100, blank=True)
    # Usamos CharField para categorías

    def __str__(self):
        return self.categoria
