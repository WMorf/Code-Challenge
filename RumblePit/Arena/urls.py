from django.urls import path
from . import views

urlpatterns = [
    path('', views.arena_home, name='arena_home'),
    path('create/', views.arena_create, name='arena_create'),
    path('display/', views.arena_display, name='arena_display'),
    path('<int:pk>/details/', views.arena_details, name='arena_details'),
    path('<int:pk>/edit/', views.arena_edit, name='arena_edit'),
    path('<int:pk>/delete/', views.arena_delete, name='arena_delete'),
    path('fight/', views.arena_fight_select, name='arena_fight_select'),
    path('results/', views.arena_results, name='arena_results'),
]
