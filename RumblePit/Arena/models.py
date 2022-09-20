from django.db import models

# Used to illustrate a variety of field types for models
COLORS_CHOICES = {
    ('red', 'red'),
    ('blue', 'blue'),
    ('green', 'green'),
    ('yellow', 'yellow'),
}

EQUIPMENT_CHOICES = {
    ('sword and shield', 'sword and shield'),
    ('spear and helmet', 'spear and hemet'),
    ('net and trident', 'net and trident'),
}


# Create your models here.
class Gladiator(models.Model):
    name = models.CharField(max_length=50, default="", null=False)
    age = models.IntegerField(default=20)
    colors = models.CharField(max_length=20, choices=COLORS_CHOICES)
    equipment = models.CharField(max_length=30, choices=EQUIPMENT_CHOICES)
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)

    Gladiators = models.Manager()

# returns name field for clarity
    def __str__(self):
        return self.name
