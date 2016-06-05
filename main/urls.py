from django.conf.urls import url
from . import views

urlpatterns = [
       url(r'^$', views.homeView.as_view(), name='homeView'),
]
