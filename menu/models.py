from django.db import models


class Category(models.Model):
    """
    Stores categories of dishes in menu
    """
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


# Dishes
class Food(models.Model):
    """
    Stores a single dish record related to :model:`Category`
    """
    title = models.CharField(max_length=200,)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    vegan = models.BooleanField(default=False)
    spiciness = models.IntegerField(default=0)

    def __str__(self):
        return self.title
