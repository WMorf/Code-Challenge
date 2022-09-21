from django.shortcuts import render, get_object_or_404, redirect
from .models import Gladiator
from .forms import GladiatorForm
import random


# Arena Home Page
def arena_home(request):
    return render(request, 'Arena/arena_home.html')


# Arena Create Page
def arena_create(request):
    #  form fields map to HTML form <input> elements for easy creation.
    form = GladiatorForm(data=request.POST or None)

    # return home after creating new fighter. Made automatic with redirect so user does not
    # have to manually navigate away from this page
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('arena_home')

    context = {'form': form}
    return render(request, 'Arena/arena_create.html', context)


# Arena Display Database
def arena_display(request):
    # accessing the Model Manage Gladiators allows us to use a for loop on
    # the page rather than manually assigning variables for each record in the
    # database to be displayed. This is faster and cleaner.
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

    return render(request, "Arena/arena_delete.html", context)


# Arena Fight Page
def arena_fight_select(request):
    fighters = Gladiator.Gladiators.all().order_by('wins')
    context = {"fighters": fighters}

    return render(request, "Arena/arena_fight_select.html", context)


# Arena Result Page
def arena_results(request):
    # Grabs value from selected options which is then linked to respective primary keys from database
    pk1 = request.POST.get('fighter1')
    pk2 = request.POST.get('fighter2')

    # This is done to prevent the same fighter from being used and to avoid errors updating the record
    if pk1 != pk2:
        fighter1 = get_object_or_404(Gladiator, pk=pk1)
        fighter2 = get_object_or_404(Gladiator, pk=pk2)

        # Random Coin-Flip determining victor, 0-1 range for estimated %50 chance
        coinflip = random.randint(0, 1)
        print(coinflip)

        # Wins and losses are updated depending on victor and then saved, updating the records
        # winner is assigned this way to display it after with a CSS fade in effect
        if coinflip == 0:
            fighter1.wins = fighter1.wins + 1
            fighter2.losses = fighter2.losses - 1
            fighter1.save()
            fighter2.save()
            winner = get_object_or_404(Gladiator, pk=pk1)
        else:
            fighter2.wins = fighter2.wins + 1
            fighter1.losses = fighter1.losses - 1
            fighter2.save()
            fighter1.save()
            winner = get_object_or_404(Gladiator, pk=pk2)

        context = {'fighter1': fighter1, 'fighter2': fighter2, 'winner': winner}

        return render(request, 'Arena/arena_results.html', context)

    else:
        return redirect('arena_error')


# Arena Fight Error Page
def arena_error(request):
    return render(request, 'Arena/arena_error.html')
