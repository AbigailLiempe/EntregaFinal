from AppBlog.forms import EquipoFormulario, LiderFormulario, RegistroFormulario, AvatarFormulario
from AppBlog.models import Equipo, Lider, Avatar, Colaborador
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView



def login_request(request):
      
    if request.method == 'POST':

        form = AuthenticationForm(request, data = request.POST) 

        if form.is_valid():
            
            usuario=form.cleaned_data.get('username')   
            contra=form.cleaned_data.get('password')    

            user=authenticate(username=usuario, password=contra)   
            if user:    
                login(request, user)   

                
                return render(request, "AppBlog/inicio.html", {'mensaje':f"Que bueno que llegaste {user}"}) 

        else:   
    
            return render(request, "AppBlog/inicio.html", {'mensaje':"Esos datos no son, fijate de nuevo porfa"})

    else:
            
        form = AuthenticationForm() 

    return render(request, "AppBlog/login.html", {'form':form})  


def register(request):
      
    if request.method == 'POST':    

        form = RegistroFormulario(request.POST)   

        if form.is_valid():

            user=form.cleaned_data['username']
            form.save()
            
            return render(request, "AppBlog/inicio.html", {'mensaje':"Epa! que nombre, no tenemos en ese color"})
    
    else:

        form = RegistroFormulario()   
    
    
    return render(request, "AppBlog/registro.html", {'form':form})


@login_required
def inicio(request):


    return render(request,"AppBlog/inicio.html")


@login_required
def agregarImagen(request):

    if request.method == 'POST': 

        miFormulario = AvatarFormulario(request.POST, request.FILES) 
        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            avatar = AvatarFormulario(user=request.user, imagen=informacion['imagen'])

            avatar.save()

            return render(request, "AppBlog/inicio.html")

    else:

        miFormulario = AvatarFormulario()
    
    return render(request, "AppBlog/agregarImg.html", {'form':miFormulario})



@login_required
def agregarEquipo(request):

    
    if request.method == 'POST':    

        miFormulario = EquipoFormulario(request.POST)    

        print(miFormulario)

        if miFormulario.is_valid():    

            informacion = miFormulario.cleaned_data

            curso = EquipoFormulario(nombre=informacion['nombre'], identificacion=informacion['identificacion'], area=informacion['area'])  

            curso.save()

            return render(request, "AppBlog/inicio.html")  

    else:

        miFormulario = EquipoFormulario()   
    dict1={"miFormulario":miFormulario}

    return render(request, "AppBlog/curso.html", dict1)


@login_required
def agregarPublicacion(request):

    return render(request, "AppBlog/publicacion.html")



@login_required
def agregarColaborador(request):

    return render(request, "AppBlog/colaborador.html")

def about(request):
      
    return render(request, "AppBlog/about.html")

@login_required
def busquedaEquipo(request):

    return render(request, "AppBlog/busquedaEquipo.html")

@login_required
def buscar(request):

   

    if request.GET['nombre']:

        nombre= request.GET['nombre']      #
        equipos = EquipoFormulario.objects.filter(nombre__iexact=nombre)

        return render(request, "AppBlog/resultadosBusqueda.html", {"equipos":equipos, "nombre":nombre})

    else:

        respuesta="Che! como que faltan cosas."
    
    return HttpResponse(respuesta)





@login_required
def agregarLider(request):


    if request.method == 'POST':    

        miFormulario = LiderFormulario(request.POST)

        if miFormulario.is_valid():

            info = miFormulario.cleaned_data    
            
            profe = LiderFormulario(nombre=info['nombre'], apellido=info['apellido'],
            email=info['email'],area=info['area'])

            profe.save()

            return render(request, "AppBlog/inicio.html")

    else:

        miFormulario = LiderFormulario()

    dict1={'myForm':miFormulario}

    return render(request,"AppBlog/lider.html", dict1)




@login_required
def borrarLideres(request, lider_nombre):

    lider = Lider.objects.get(nombre=lider_nombre)
    
    lider.delete()
    
    lideres = lider.objects.all()

    contexto={"lideres":lideres}

    return render(request, "AppBlog/leerLideres.html",contexto)


@login_required
def editarLideres(request, lider_nombre, lider=None):

    lider = lider.objects.get(nombre=lider_nombre)

    if request.method == "POST":

        miFormulario = LiderFormulario(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            lider.nombre = informacion['nombre']
            lider.apellido = informacion['apellido']
            lider.email = informacion['email']
            lider.area = informacion['area']

            lider.save()

            return render(request, "AppBlog/inicio.html")

    else:

        miFormulario= LiderFormulario(initial={'nombre':lider.nombre, 'apellido':lider.apellido,
        'email':lider.email, 'area':lider.area})

    return render(request, "AppBlog/editarLider.html",{'miFormulario':miFormulario, 'lider_nombre':lider_nombre})



@login_required

def listaLideres(request):

    lideres = Lider.objects.all() 


    contexto = {"Lider":lideres}
    return render(request, "AppBlog/leerLideres.html",contexto)





@login_required
def editarUsuario(request):

    usuario = request.user 
    if request.method == "POST":   

        miFormulario = RegistroFormulario(request.POST) 

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data    

            #actualizar la info del usuario activo
            usuario.username = informacion['username']
            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password1']
            usuario.save()

            return render(request, "AppBlog/inicio.html")

    else:

        miFormulario= RegistroFormulario(initial={'username':usuario.username, 'email':usuario.email})

    return render(request, "AppBlog/editarUsuario.html",{'miFormulario':miFormulario, 'usuario':usuario.username})


#Equipos
class EquipoList(LoginRequiredMixin, ListView):

    model = Equipo
    template_name = "AppBlog/listaEquipo.html"


class EquipoDetalle(DetailView):

    model = Equipo
    template_name = "AppBlog/equipoDetalle.html"



class EquipoCreacion(CreateView):

    model = Equipo
    success_url = "AppBlog/equipo/lista"
    fields = ['nombre', 'identificacion', 'area']


class EquipoUpdate(UpdateView):

    model = Equipo
    success_url = "AppBlog/equipo/lista"
    fields = ['nombre', 'identificacion', 'area']


class EquipoDelete(DeleteView):

    model = Equipo
    success_url = "AppBlog/equipo/lista"



class ColaboradorLista(LoginRequiredMixin, ListView):

    model = Colaborador
    template_name = "AppBlog/listacolaborador.html"



def VerAbout(request):
      
    return render(request, "AppBlog/about.html")