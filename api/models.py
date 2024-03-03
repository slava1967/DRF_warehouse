from django.contrib.auth.models import AbstractUser
from django.db import models


class ApiUser(AbstractUser):
    POSITION = [
        ('SU', 'Supplier'),
        ('CO', 'Consumer'),
    ]
    position = models.CharField(max_length=2, choices=POSITION, default='SU')


class Warehouse(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    name = models.CharField(max_length=128)
    warehouse = models.ForeignKey(Warehouse, related_name="products", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    user = models.ForeignKey(ApiUser, related_name="products", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}, {self.warehouse}"


class Order(models.Model):
    product = models.ForeignKey(Product, related_name="orders", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    # warehouse = models.ForeignKey(Warehouse, related_name="orders", on_delete=models.CASCADE)
    user = models.ForeignKey(ApiUser, related_name="orders", on_delete=models.CASCADE)
