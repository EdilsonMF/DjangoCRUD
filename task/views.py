from http.client import HTTPResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import TaskForm,CategoryForm
from .models import Task,Category
from django.utils import timezone
from django.contrib.auth.decorators import login_required

@login_required
def create_category(request):
    if request.method == 'GET':
        return render(request, 'create_category.html', {
            'form': CategoryForm
        })
    else:
        try:
            form = CategoryForm(request.POST)
            if form.is_valid():
                new_category = form.save()
                return redirect('categories')  # Redirige a la lista de categorías
            else:
                return render(request, 'create_category.html', {
                    'form': form,
                    'error': 'Por favor ingrese datos válidos'
                })
        except ValueError:
            return render(request, 'create_category.html', {
                'form': CategoryForm,
                'error': 'Hubo un problema al guardar la categoría. Intente de nuevo.'
            })

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {
        'categories': categories
    })
# Create your views here.
def home(request): 
    return render(request,'home.html')

def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html',{
            'form': UserCreationForm
        })
    else:
        if request.POST['password1']== request.POST['password2']:
            try:
                user=User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('tasks')        
            except IntegrityError:
                return render(request, 'signup.html',{
                    'form': UserCreationForm,
                    'error': 'Username already exist'
                })
        return render(request, 'signup.html',{
                    'form': UserCreationForm,
                    'error': 'Password do not match'
        })

@login_required   
def tasks(request):
    tasks=Task.objects.filter(user=request.user, datecompleted__isnull=True)
    
    return render(request, 'tasks.html', {'tasks': tasks})

@login_required 
def tasks_completed(request):
    tasks=Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    
    return render(request, 'tasks.html', {'tasks': tasks})

@login_required
def create_task(request):
    categories = Category.objects.all()  # Obtener todas las categorías de la base de datos

    if request.method == 'GET':
        form = TaskForm()  # Crear una instancia del formulario
        return render(request, 'create_task.html', {
            'form': form,
            'categories': categories,  # Pasa las categorías al contexto
        })
    else:
        form = TaskForm(request.POST)  # Crear el formulario con los datos enviados
        if form.is_valid():
            new_task = form.save(commit=False)  # Guardar la tarea pero sin commit
            new_task.user = request.user  # Asignar el usuario actual como autor de la tarea
            new_task.save()  # Guardar la tarea en la base de datos
            return redirect('tasks')  # Redirigir al listado de tareas
        else:
            return render(request, 'create_task.html', {
                'form': form,
                'categories': categories,  # Pasa las categorías de nuevo en caso de error
                'error': 'Please provide valid data'  # Mensaje de error si el formulario no es válido
            })




@login_required  
def task_detail(request, task_id):
    if request.method == 'GET':
        task= get_object_or_404(Task,pk=task_id, user=request.user)
        form=TaskForm(instance=task)
        return render(request,'task_detail.html', {'task': task, 'form': form})
    else:
        try:
            task=get_object_or_404(Task, pk=task_id, user=request.user)
            form=TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request,'task_detail.html', {'task': task, 'form': form, 'error':"Error updating task"})

@login_required 
def complete_task(request, task_id):
    task= get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method =='POST':
        task.datecompleted=timezone.now()
        task.save()
        return redirect('tasks')

@login_required     
def delete_task(request, task_id):
    task= get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method =='POST':
        task.delete()
        return redirect('tasks')
                  
         
@login_required         
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method =='GET':
        return render(request, 'signin.html',{
        'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        
        if user is None:
            return render(request, 'signin.html',{
                'form': AuthenticationForm,
                'error': 'User name or password incorrect'
            })
        else:
            login(request,user)
            return redirect('tasks')

@login_required        
def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'category_detail.html', {'category': category})

# Vista para eliminar una categoría
@login_required
def delete_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    category.delete()
    return redirect('categories_list')  # Redirige a la lista de categorías

     
@login_required
def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'categories_list.html', {'categories': categories})

@login_required
def edit_category(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('category_detail', category_id=category.id)  # Redirige a los detalles de la categoría editada
    else:
        form = CategoryForm(instance=category)
    return render(request, 'edit_category.html', {'form': form, 'category': category})
       