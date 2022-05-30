from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from AppBlog.models import Avatar

class EquipoFormulario(forms.Form):

    curso = forms.CharField(max_length=30)
    identificacion = forms.IntegerField()
    area = forms.IntegerField()

class LiderFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    area = forms.CharField()

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