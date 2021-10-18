from django.db import models
from django.db.models.deletion import PROTECT
# Create your models here.
len_medium = 50
len_medium = 5000
len_max = 10000


class User(models.Model):
    full_name = models.CharField(max_length=len_medium)
    email = models.EmailField(null=False, default='test@gmail.com')
    user_name = models.CharField(
        max_length=len_medium, unique=True, null=False)
    password = models.CharField(max_length=len_medium, null=False, default='1')


class Technology(models.Model):
    name = models.CharField(max_length=len_medium)


class Field(models.Model):
    name = models.CharField(max_length=len_medium)


class Mentor(models.Model):
    user_id = models.OneToOneField(User, unique=True, on_delete=models.PROTECT)
    contact = models.JSONField(null=True)
    description = models.TextField(max_length=len_medium)
    price = models.FloatField(null=False, default=0)
    status = models.BooleanField(default=True)
    fields = models.ManyToManyField(Field)
    technologies = models.ManyToManyField(Technology)


class Booking(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=PROTECT)
    mentee = models.ForeignKey(User, on_delete=PROTECT)
    mentor_time = models.DateTimeField(null=True)
    mentee_time = models.DateTimeField(null=True)
    time_start = models.DateTimeField(null=True)
    duration = models.PositiveSmallIntegerField(null=True)

    class Status(models.TextChoices):
        PE = "pending"
        OG = "ongoing"
        FI = "finish"
        CA = "cancel"

    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.PE)
