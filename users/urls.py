from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path('register/', views.CustomUserCreate.as_view(), name="create_user"),
    path('profile/<str:email>/', views.UserDetail.as_view(), name="user_detail"),
]