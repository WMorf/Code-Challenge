from django.db import models


# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=50, default="", null=False)
    cost = models.IntegerField(default=1)

    Foods = models.Manager()

# returns name field for clarity
    def __str__(self):
        return self.name