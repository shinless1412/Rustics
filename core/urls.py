"""
URL configuration for RusticaWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import home,products,perfil,exit,register,about,agregar_producto,restar_producto,eliminar_producto,limpiar_carrito
from .views import crear,listado,editar,eliminar
from . import views





from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('perfil/', perfil, name='perfil'),
    path('logout/', exit , name='exit'),
    path('register/', register , name='register'),
    path('about/', about , name='about'),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
 #   path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),

    path('cerveza/crear', crear, name='crear'),
    path('listado/', listado, name='listado'),
    path('cerveza/editar/', editar, name='editar'),
    path('cerveza/editar/<int:id>/', editar, name='editar_id'),
    path('eliminar/<int:id>/', eliminar, name='eliminar'),
    path('reviews/<int:producto_id>/', views.lista_reviews, name='lista_reviews'),
    path('reviews/<int:review_id>/eliminar/', views.eliminar_review, name='eliminar_review'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
