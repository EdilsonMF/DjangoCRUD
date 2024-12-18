from django.forms import ModelForm
from .models import Task,Category
from django import forms


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'category', 'important', 'borrador', 'publicado']
    
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=True)
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['categoria', 'subcategoria']
        widgets = {
            'categoria': forms.TextInput(attrs={'placeholder': 'Enter category name'}),
            'subcategoria': forms.TextInput(attrs={'placeholder': 'Enter subcategory name'}),
        }