from django.db import models
from django.utils import timezone
from django.conf import settings
# Create your models here.

class Photo(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField(default=timezone.now)
    pixel_width = models.IntegerField()
    pixel_height = models.IntegerField()
    iso = models.IntegerField()
    focal_length = models.CharField()
    f_number = models.CharField()
    exposure_time = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    theme = models.CharField(max_length=200)
    topic = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(null=True, blank=True)
    def __str__(self):
        return self.title
    
# class Topic(models.Model):
#     name = models.CharField(max_length=200)
#     def __str__(self):
#         return self.name
    
class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, to_field= 'email', on_delete=models.CASCADE)
    time = models.DateTimeField(default=timezone.now)
    bill_name = models.CharField(max_length=200)
    bill_address = models.CharField(max_length=200)
    photos = models.ManyToManyField(Photo)
    total = models.IntegerField()
    def __str__(self):
        return self.user.email + " " + str(self.time)
    
# class Item(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.CASCADE)
#     photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
#     def __str__(self):
#         return self.photo.title
