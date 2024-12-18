from django.contrib import admin
from .models import Task,Author,Category

class TaskAdmin(admin.ModelAdmin):
    readonly_fields=('created', )
    
# Register your models here.
admin.site.register(Task,TaskAdmin)
admin.site.register(Author)

# Registrar el modelo Category
admin.site.register(Category)
