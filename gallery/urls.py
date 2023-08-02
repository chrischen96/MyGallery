from django.urls import path
from . import views

urlpatterns = [
    path('', views.PhotoList.as_view()),
    path('photos/', views.PhotoList.as_view()),
    path('photos/theme/<str:theme>', views.PhotoListByTheme.as_view()),
    path('photos/<int:pk>/', views.PhotoDetail.as_view()),
    path('orders/', views.OrderList.as_view()),
    path('orders/<int:pk>/', views.OrderDetail.as_view()),
    path('cart/', views.CartList.as_view()),
    path('cart/<str:email>/', views.CartDetail.as_view()),
]