from django.db import models

# Create your models here.

class Photo(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField('date published')
    pixel_width = models.IntegerField()
    pixel_height = models.IntegerField()
    focal_length = models.IntegerField()
    f_number = models.CharField(max_length=200)
    iso = models.IntegerField()
    exposure_time = models.CharField(max_length=200)
    # location = models.CharField(max_length=200)
    # description = models.CharField(max_length=200)
    # topic = models.ForeignKey('topic', on_delete=models.CASCADE)
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    # image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name
    
# class Topic(models.Model):
#     name = models.CharField(max_length=200)
#     def __str__(self):
#         return self.name
    
class Order(models.Model):
    name = models.CharField(max_length=200)
    time = models.DateTimeField('date published')
    total = models.IntegerField()
    payment = models.CharField(max_length=200)
    def __str__(self):
        return self.name
    
class Item(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
