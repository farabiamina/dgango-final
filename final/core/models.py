from django.db import models
from django.utils.timezone import now
# Create your models here.


class BookJournalBase(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField
    description = models.CharField(max_length=250)
    created_at = models.DateTimeField(default=now)

    class Meta:
        abstract = True


class Book(BookJournalBase):
    num_pages = models.IntegerField
    genre = models.CharField(max_length=100)


class Journal(BookJournalBase):
    class Type(models.TextChoices):
        bullet = "Bullet"
        food = "Food"
        travel = "Travel"
        sport = "Sport"
    type = models.CharField(max_length=100, choices=Type.choices, default=Type.bullet)
    publisher = models.CharField(max_length=100)

