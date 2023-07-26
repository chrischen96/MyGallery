from django.contrib import admin
from .models import Photo, Order, Item

# Register your models here.
admin.site.register(Photo)
admin.site.register(Order)
admin.site.register(Item)