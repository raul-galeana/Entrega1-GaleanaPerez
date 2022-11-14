from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('nosotrxs/', views.nosotrxs, name='nosotrxs'),
    path('ver-mascotas/', views.VerMascotas.as_view(), name='ver_mascotas'),
    path('alta-mascota/', views.AltaMascota.as_view(), name='alta_mascota'),
    path('editar-mascota/<int:pk>', views.EditarMascota.as_view(), name='editar_mascota'),
    path('eliminar-mascota/<int:pk>', views.EliminarMascota.as_view(), name='eliminar_mascota')
]