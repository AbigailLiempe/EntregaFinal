from django.urls import path
from AppBlog import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("", views.inicio, name='Inicio'),
    path("buscar/", views.buscar),
    
    
    path("addColaborador/", views.agregarColaborador, name="addColaboradores"),
    path("addPublicacion/", views.agregarPublicacion, name='addPublicacion'),
    #path('colab/lista', views.ColaboradorLista.as_view(), name='listacolaborador'),

    path("addLider/", views.agregarLider, name='addLideres'),
    path("listaLider", views.listaLideres, name="ListaLideres"),
    path("chauLider/<lider_nombre>", views.borrarLideres, name="BorrarLider"),
    path("editarLider/<lider_nombre>", views.editarLideres, name="EditarLideres"),

    path("addEquipos/", views.agregarEquipo, name='addEquipo'),    
    path("busquedaEquipo/", views.busquedaEquipo, name="BusquedaEquipo"),
    path('equipo/lista', views.EquipoList.as_view(), name='ListEquipo'),
    path(r'^(?P<pk>\d+)$', views.EquipoDetalle.as_view(), name='Detail'),
    path(r'^nuevo$', views.EquipoCreacion.as_view(), name='New'),
    path(r'^editar/(?P<pk>\d+)$', views.EquipoUpdate.as_view(), name='Edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.EquipoDelete.as_view(), name='Delete'),

    path('login', views.login_request, name = 'Login'),
    path('logout', LogoutView.as_view(template_name='AppBlog/logout.html'), name='Logout'),
    path('register', views.register, name = 'Register'),
    path("editarUsuario", views.editarUsuario, name="EditarUsuario"),
    path('agregarimagen/', views.agregarImagen, name='Subir Avatar'),
    
]