from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.


# Table model
class Table(models.Model):
    """
    Stores available tables and their capacity
    """
    table_number = models.CharField(max_length=200, unique=True)
    capacity = models.IntegerField(default=2)

    def __str__(self):
        return f'Table {self.table_number} for {self.capacity}'

# Booking model
class Reservation(models.Model):
    """
    Stores a single table booking record related to :model:`Table`
    """
    party_size = models.IntegerField()
    date_time = models.DateTimeField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    comments = models.TextField(blank=True)
    table_number = models.ManyToManyField(Table)
    reference = models.CharField(max_length=8, unique=True)
    cancelled_by_user = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.pk:
            self.reference = str(uuid.uuid4())[:8]
        super().save(*args, **kwargs)
