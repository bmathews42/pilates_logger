from django.db import models

# Create your models here.
from django.db import models


class Instructor(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class PilatesClass(models.Model):

    DIFFICULTY = [
        (1, "Easy"),
        (2, "Medium"),
        (3, "Hard"),
        (4, "Death 💀"),
    ]

    date = models.DateField()

    instructor = models.ForeignKey(
        Instructor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    arms = models.IntegerField(choices=DIFFICULTY, default=0)
    legs = models.IntegerField(choices=DIFFICULTY, default=0)
    abs = models.IntegerField(choices=DIFFICULTY, default=0)
    obliques = models.IntegerField(choices=DIFFICULTY, default=0)

    calories = models.IntegerField(default=0)

    notes = models.TextField(blank=True)

    created = models.DateTimeField(auto_now_add=True)