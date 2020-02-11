from django.db import models
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255)
class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    customer = models.OneToOneField(
        Customer,
        on_delete=models.CASCADE,
        related_name='vehicle')