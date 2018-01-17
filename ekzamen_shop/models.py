from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=450, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    images = models.ImageField(upload_to='media')
    in_stock = models.IntegerField()
    category = models.ForeignKey(Category, to_field='name', related_name='category', )

    def __str__(self):
        return self.name


class ExampleBasket(models.Model):
    owner = models.ForeignKey('auth.User', related_name='users', on_delete=models.CASCADE)
    quantity = models.IntegerField()
    product = models.ForeignKey(Products, to_field='name', )
    price = models.DecimalField(decimal_places=2, max_digits=6, )

    def __str__(self):
        return self.product.name


class Basket(models.Model):
    user = models.ForeignKey('auth.User', related_name='user', on_delete=models.CASCADE)
    elements = models.ForeignKey(ExampleBasket, related_name='element')
    status = models.BooleanField(default=False)
