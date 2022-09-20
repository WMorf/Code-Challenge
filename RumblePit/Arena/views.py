from django.shortcuts import render, HttpResponse


# Arena Home Page
def arena_home(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'Arena/arena_home.html')
