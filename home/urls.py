from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ver-mascotas/', views.ver_mascotas, name='ver_mascotas'),
    path('alta-mascota/', views.alta_mascota, name='alta_mascota'),
]