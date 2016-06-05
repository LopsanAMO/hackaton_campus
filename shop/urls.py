from django.conf.urls import url
from . import views

urlpatterns = [

       url(r'^productos/', views.ProductoView.as_view(), name='productos'),
       url(r'^detalle/', views.detalleView.as_view(), name='detalle'),
       url(r'^artesanal/', views.artesalanView.as_view(), name='box'),


]
