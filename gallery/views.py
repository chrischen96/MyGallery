from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo, Order
from rest_framework import generics
from .serializers import PhotoSerializer, OrderSerializer
from rest_framework.permissions import SAFE_METHODS, IsAuthenticated, BasePermission, IsAdminUser, AllowAny, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.

class OrderUserPermission(BasePermission):
    message = 'Editing orders is restricted to the user who created the order.'
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class PhotoList(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = (JWTAuthentication,)

class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = (JWTAuthentication,)

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = (JWTAuthentication,)

    # def get_queryset(self):
    #     user = self.request.user
    #     return Order.objects.filter(user=user)

class OrderDetail(generics.RetrieveUpdateDestroyAPIView, OrderUserPermission):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = [IsAuthenticated&OrderUserPermission]
    authentication_classes = (JWTAuthentication,)

# class ItemList(generics.ListCreateAPIView):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer
#     authentication_classes = (JWTAuthentication,)

# class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Item.objects.all()
#     serializer_class = ItemSerializer
#     authentication_classes = (JWTAuthentication,)
