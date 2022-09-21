from django.urls import path
from . import views

urlpatterns = [
    path('', views.food_home, name='food_home'),
    path('create/', views.food_create, name='food_create'),
    path('display/', views.food_display, name='food_display'),
    path('<int:pk>/details/', views.food_details, name='food_details'),
    path('<int:pk>/edit/', views.food_edit, name='food_edit'),
    path('<int:pk>/delete/', views.food_delete, name='food_delete'),
]