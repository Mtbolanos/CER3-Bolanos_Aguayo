from django import forms
from .models import Produccion
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProduccionForm(forms.ModelForm):
    class Meta:
        model = Produccion
        fields = ['planta', 'producto', 'cantidad']

class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']