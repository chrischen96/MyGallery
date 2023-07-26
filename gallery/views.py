from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo, Order, Item
from rest_framework import generics
from .serializers import PhotoSerializer, OrderSerializer, ItemSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class PhotoList(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    # permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    # permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    # permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)

class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    # permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
