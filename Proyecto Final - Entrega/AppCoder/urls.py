from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('',views.inicio,name='inicio'),        # Modifciado el 14/12
    #----------------------
    #  Mascotas
    #----------------------
    path('mascota',views.animal,name='mascota'),
    path('formularioMascota',views.formularioMascota,name='formularioMascota'),
    path('leerMascota',views.leerMascota,name='leerMascota'),
    path('eliminarMascota/<mascota_nombre>/',views.eliminarMascota,name='eliminarMascota'),
    path('editarMascota/<mascota_nombre>/',views.editarMascota,name='editarMascota'),
    path('busquedaMascota',views.busquedaMascota,name='busquedaMascota'),
    path('buscar/',views.buscar),
    #----------------------
    #  Personas
    #----------------------
    path('persona',views.persona,name='persona'),
    path('formularioPersona',views.formularioPersona,name='formularioPersona'),
    path('leerPersona',views.leerPersona,name='leerPersona'), 
    path('eliminarPersona/<persona_nombre>/',views.eliminarPersona,name='eliminarPersona'),
    path('editarPersona/<persona_nombre>/',views.editarPersona,name='editarPersona'),
    #----------------------
    #  Veterinarios
    #----------------------
    path('veterinario',views.veterinario,name='veterinario'),
    path('formularioVeterinario',views.formularioVeterinario,name='formularioVeterinario'),
    path('leerVeterinario',views.leerVeterinario,name='leerVeterinario'), 
    #----------------------
    #  Login/Registro
    #----------------------
    path('login',views.login_request, name='Login'),
    path('register',views.register, name='Register'),
    path('logout',LogoutView.as_view(template_name='AppCoder/logout.html'), name='Logout'),
    path('editarPerfil', views.editarPerfil, name="EditarPerfil"),    

    #----------------------
    #  Extras
    #----------------------
    path('about', views.about, name="about"),
]