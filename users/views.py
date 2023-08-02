from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly, BasePermission, SAFE_METHODS
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import NewUser
from .serializers import UserSerializer
from .serializers import RegisterUserSerializer

class DefaultUserPermission(BasePermission):
    message = 'Editing users is restricted to the user who created the user.'
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.email == request.email

class CustomUserCreate(APIView):
    # permission_classes = (AllowAny)
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserDetail(generics.RetrieveUpdateDestroyAPIView, DefaultUserPermission):
    queryset = NewUser.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = [IsAuthenticated&DefaultUserPermission]