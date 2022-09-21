from django.forms import ModelForm
from .models import Gladiator


class GladiatorForm(ModelForm):
    class Meta:
        model = Gladiator
        fields = '__all__'
