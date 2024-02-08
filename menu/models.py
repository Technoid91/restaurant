from django.db import models

# Create your models here.

# Menu categories
class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


# Dishes
class Food(models.Model):
    title = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    vegan = models.BooleanField(default=False)
    spiciness = models.IntegerField(default=0)

    def __str__(self):
        return self.title