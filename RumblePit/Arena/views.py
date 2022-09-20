from django.shortcuts import render, HttpResponse


# Arena Home Page
def arena_home(request):
    return render(request, 'Arena/arena_home.html')
