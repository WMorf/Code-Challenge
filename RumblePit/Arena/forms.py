from django.forms import ModelForm
from .models import Gladiator


# name of model with "form" added again for clarity. Allows for easy display on page and saving records
class GladiatorForm(ModelForm):
    class Meta:
        model = Gladiator
        fields = '__all__'
