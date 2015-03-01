from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    pass

class Store(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()

    company = models.ForeignKey(Company)

class Aisle(models.Model):
    name = models.CharField(max_length=255)

    store = models.ForeignKey(Store)


class FoodItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    cost = models.IntegerField()

    aisle = models.ForeignKey(Aisle, related_name="food_items")

