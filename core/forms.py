from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Producto
from .models import Review

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','password1', 'password2']
        
class CervezaForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['contenido', 'puntuacion']

