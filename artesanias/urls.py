from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('main.urls', namespace='home')),
    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^shop/', include('shop.urls', namespace='shop')),
    url(r'^orders/', include('orders.urls', namespace='orders')),
    url(r'^login/', include('login.urls', namespace='login'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
