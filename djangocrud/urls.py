"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/',views.signup, name='signup'),
    path('tasks/',views.tasks, name='tasks'),
    path('tasks_completed/',views.tasks_completed, name='tasks_completed'),
    path('logout/',views.signout, name='logout'),
    path('signin/',views.signin ,name='signin'),
    path('tasks/create/',views.create_task ,name='create_task'),
    path('tasks/<int:task_id>/',views.task_detail ,name='task_detail'),
    path('tasks/<int:task_id>/complete',views.complete_task ,name='complete_task'),
    path('tasks/<int:task_id>/delete',views.delete_task ,name='delete_task'),
    path('create_category/', views.create_category, name='create_category'),
    path('categories/', views.category_list, name='categories'),
    
    path('categories/', views.categories_list, name='categories_list'),  # Lista de categorías
    path('categories/<int:category_id>/', views.category_detail, name='category_detail'),  # Ver detalles de la categoría
    path('categories/<int:category_id>/edit/', views.edit_category, name='edit_category'),  # Editar categoría
    path('categories/<int:category_id>/delete', views.delete_category, name='delete_category'),  # Eliminar categoría




]