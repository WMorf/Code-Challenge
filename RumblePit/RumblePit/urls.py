from django.contrib import admin
from django.urls import include, path
from . import views

# Points user to the correct app
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('Arena/', include('Arena.urls')),
    path('Food/', include('Food.urls')),
]
