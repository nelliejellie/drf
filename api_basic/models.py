from django.db import models
from cloudinary.models import CloudinaryField
import cloudinary
# signal import
from django.db.models.signals import pre_delete
from django.dispatch import receiver
# settings import
from django.conf import settings

# Create your models here.

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='current_user', on_delete=models.CASCADE)
    status_choices = (
        ('not selected', 'not selected'),
        ('EndSars', 'EndSars'),
        ('Covid-19', 'Covid-19')
    )
    quote = models.TextField(max_length=500)
    author =  models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    image = CloudinaryField('image', default='https://res.cloudinary.com/dhfao0jm7/image/upload/v1607673363/noImage_ipctvi.jpg')
    categories = models.CharField(max_length=30, choices=status_choices,default='not selected')
    legit = models.BooleanField(default=False)

    def __str__(self):
        return self.author

# the api endpoints 
class Api_Urls(models.Model):
    url_title = models.CharField(max_length=50,blank=True)
    url = models.URLField(max_length=50)
    how_to_use = models.TextField(max_length=300, blank=True)

    def __str__(self):
        return self.url_title


# signal to delete image from cloudinary if user deletes an object
@receiver(pre_delete, sender=Article)
def photo_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.image.public_id)
