from django.urls import path
from . import views

urlpatterns = [
    path('', views.PhotoList.as_view()),
    path('photos/', views.PhotoList.as_view()),
    path('photos/<int:pk>/', views.PhotoDetail.as_view()),
    path('orders/', views.OrderList.as_view()),
    path('orders/<int:pk>/', views.OrderDetail.as_view()),
    # path('items/', views.ItemList.as_view()),
    # path('items/<int:pk>/', views.ItemDetail.as_view()),
]