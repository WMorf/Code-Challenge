from django.urls import path
from . import views

urlpatterns = [
    path('', views.arena_home, name='arena_home'),
]
