from re import T
from django.db import models
from django.db.models.deletion import PROTECT
# Create your models here.
len_medium = 50
len_medium = 5000
len_max = 10000


class User(models.Model):
    email = models.EmailField(null=True, unique=True)
    image = models.URLField(null=True)
    money = models.IntegerField(default=0)
    user_name = models.CharField(max_length=len_medium, null=True)
    gg_id = models.CharField(max_length=len_medium, null=True, default='gg_id')
    password = models.CharField(max_length=len_medium, null=False, default='1')


class Technology(models.Model):
    name = models.CharField(max_length=len_medium)


class Field(models.Model):
    name = models.CharField(max_length=len_medium)


class Mentor(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.PROTECT)
    full_name = models.CharField(max_length=len_medium, null=True)
    thumbnail = models.URLField(null=True)
    contacts = models.JSONField(null=True)
    description = models.TextField(null=True, max_length=len_medium)
    price = models.IntegerField(default=0)
    status = models.BooleanField(default=True)
    fields = models.ManyToManyField(Field, null=True)
    technologies = models.ManyToManyField(Technology, null=True)


class Status(models.TextChoices):
    OG = "ongoing"
    FI = "finish"
    CA = "cancel"


class Booking(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=PROTECT)
    mentee = models.ForeignKey(User, on_delete=PROTECT)
    mentor_time = models.DateTimeField(null=True)
    mentee_time = models.DateTimeField(null=True)
    time_start = models.DateTimeField(null=True, auto_now_add=True)
    duration = models.PositiveSmallIntegerField(null=True)
    total_price = models.IntegerField(default=0)

    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.OG)


class Rating(models.Model):
    booking = models.OneToOneField(Booking, unique=True, on_delete=PROTECT)
    rating = models.IntegerField(default=0)
    comment = models.TextField(null=True)
