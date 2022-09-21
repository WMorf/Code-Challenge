from django.shortcuts import render, get_object_or_404, redirect
from .models import Food
from .forms import FoodForm


# Food Home Page
def food_home(request):
    return render(request, 'Food/food_home.html')


# Food Create Page
def food_create(request):
    form = FoodForm(data=request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('food_home')

    context = {'form': form}
    return render(request, 'Food/food_create.html', context)


# Food Display Database
def food_display(request):
    eddibles = Food.Foods.all()
    context = {'eddibles': eddibles}

    return render(request, 'Food/food_display.html', context)


# Food Details Page
def food_details(request, pk):
    pk = int(pk)
    eddible = get_object_or_404(Food, pk=pk)
    context = {'eddible': eddible}

    return render(request, 'Food/food_details.html', context)


# Food Edit Page
def food_edit(request, pk):
    pk = int(pk)
    eddible = get_object_or_404(Food, pk=pk)
    form = FoodForm(data=request.POST or None, instance=eddible)

    # return home after updating new food
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('food_home')

    context = {'form': form, "eddible": eddible}

    return render(request, 'Food/food_edit.html', context)


# Food Delete Page
def food_delete(request, pk):
    pk = int(pk)
    eddible = get_object_or_404(Food, pk=pk)
    context = {"eddible": eddible}
    eddible.delete()

    return render(request, "Food/food_delete.html", context)
