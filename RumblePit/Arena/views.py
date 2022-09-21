from django.shortcuts import render, get_object_or_404, redirect
from .models import Gladiator
from .forms import GladiatorForm
import random


# Arena Home Page
def arena_home(request):
    return render(request, 'Arena/arena_home.html')


# Arena Create Page
def arena_create(request):
    form = GladiatorForm(data=request.POST or None)

    # return home after creating new fighter with redirect
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('arena_home')

    context = {'form': form}
    return render(request, 'Arena/arena_create.html', context)


# Arena Display Database
def arena_display(request):
    fighters = Gladiator.Gladiators.all()
    context = {'fighters': fighters}

    return render(request, 'Arena/arena_display.html', context)


# Arena Details Page
# Lets user view details of created fighter using its Primary Key
def arena_details(request, pk):
    pk = int(pk)
    fighter = get_object_or_404(Gladiator, pk=pk)
    context = {'fighter': fighter}

    return render(request, 'Arena/arena_details.html', context)


# Arena Edit Page
def arena_edit(request, pk):
    pk = int(pk)
    fighter = get_object_or_404(Gladiator, pk=pk)
    form = GladiatorForm(data=request.POST or None, instance=fighter)

    # return home after updating new fighter with redirect
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('arena_home')

    context = {'form': form, "fighter": fighter}

    return render(request, 'Arena/arena_edit.html', context)


# Arena Delete Page
def arena_delete(request, pk):
    pk = int(pk)
    fighter = get_object_or_404(Gladiator, pk=pk)
    context = {"fighter": fighter}
    fighter.delete()

    return render(request, "/Arena/arena_delete.html", context)


def arena_fight_select(request):
    fighters = Gladiator.Gladiators.all().order_by('wins')
    context = {"fighters": fighters}

    return render(request, "Arena/arena_fight_select.html", context)


def arena_results(request):
    if request.method == 'POST':
        pk1 = request.POST.get('fighter1')
        pk2 = request.POST.get('fighter2')
        fighter1 = get_object_or_404(Gladiator, pk=pk1)
        fighter2 = get_object_or_404(Gladiator, pk=pk2)
        context = {'fighter1': fighter1, 'fighter2': fighter2}

    return render(request, 'Arena/arena_results.html', context)
