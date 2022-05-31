from django.contrib import admin

# Register your models here.
from django.contrib import admin

from AppBlog.views import about
from .models import *

# Register your models here.

admin.site.register(Equipo)
admin.site.register(Lider)
admin.site.register(Publicaciones)
admin.site.register(Colaborador)
admin.site.register(Avatar)
