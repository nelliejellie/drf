from django.db import models
from cloudinary.models import CloudinaryField
# signal import
from django.db.models.signals import pre_delete
from django.dispatch import receiver

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    author =  models.CharField(max_length=100)
    email = models.EmailField(max_length=30)
    date = models.DateField(auto_now_add=True)
    image = CloudinaryField('image', blank=True)

    def __str__(self):
        return self.title


# signal to delete image from cloudinary if user deletes an object
@receiver(pre_delete, sender=Article)
def photo_delete(sender, instance, **kwargs):
    cloudinary.uploader.destroy(instance.image.public_id)
