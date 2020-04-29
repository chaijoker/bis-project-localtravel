from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Trip(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=30, null=True)
    place = models.CharField(max_length=30, null=True)
    detail_place = models.TextField(null=True)
    detail_trip = models.TextField(null=True)
    price_trip = models.FloatField(null=True)
    type_price = models.CharField(max_length=5, null=True)
    phone = models.CharField(max_length=10, null=True)
    date = models.DateField(auto_now_add=True, null=True)
    time_start =models.TimeField(null=True)
    time_end =models.TimeField(null=True)
    image_trip =models.ImageField(null=True)
    booking_status =models.BooleanField(default=True)


class Guide(models.Model):
    first_name = models.CharField(max_length=40, null=True)
    last_name = models.CharField(max_length=40, null=True)
    username = models.CharField(max_length=40, null=True)
    password = models.CharField(max_length=40, null=True)
    email = models.TextField(null=True)
    telephone = models.CharField(max_length=10, null=True)
    nationalID = models.CharField(max_length=20, null=True)

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    image_pay = models.ImageField(null=True)


