from django.urls import path
from home import views

urlpatterns = [
    # Version vistas comunes -----------
    # path('', views.index, name='index'),
    # path('ver-mascotas/', views.ver_mascotas, name='ver_mascotas'),
    # path('alta-mascota/', views.alta_mascota, name='alta_mascota'),
    # path('editar-mascota/<int:id>', views.editar_mascota, name='editar_mascota'),
    # path('eliminar-mascota/<int:id>', views.eliminar_mascota, name='eliminar_mascota'),
    
    #Version clases basadas en vistas
    path('', views.index, name='index'),
    path('ver-mascotas/', views.VerMascotas.as_view(), name='ver_mascotas'),
    path('alta-mascota/', views.AltaMascota.as_view(), name='alta_mascota'),
    path('editar-mascota/<int:pk>', views.EditarMascota.as_view(), name='editar_mascota'),
    path('eliminar-mascota/<int:pk>', views.EliminarMascota.as_view(), name='eliminar_mascota')
]