from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


# News model
class New(models.Model):
    """
    Stores news and special offers objects to
    represent them on the home page

    """
    title = models.CharField(max_length=200, unique=True)
    image = CloudinaryField('image', default='placeholder')
    text = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
