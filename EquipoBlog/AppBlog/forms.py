from dataclasses import field
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppBlog.models import Avatar, Publicaciones


class EquipoFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    identificacion = forms.IntegerField()
    area = forms.IntegerField()

class LiderFormulario(forms.Form):

    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    area = forms.CharField(max_length=30)

class RegistroFormulario(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:

        model = User
        fields = ['username', 'email', 'password1', 'password2'] 


class AvatarFormulario(forms.ModelForm):

    class Meta:

        model = Avatar
        fields = ['user', 'imagen']
        
        
class PubliForm(forms.ModelForm):
      
    contenido = forms.CharField(label='',widget=forms.Textarea(attrs={'rows':2,'placeholder':'Info'}),required=True)   
    
    class Meta:
        model = Publicaciones
        fields = ['contenido'] 
        