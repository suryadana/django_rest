from django.contrib.auth.hashers import make_password

from rest_framework import generics, permissions
from rest_framework_jwt.views import JSONWebTokenAPIView

from authentication.serializer import (
	User, UserSerializer,
	UserJWTSerializer
)

# Create your views here.
class UserCreateAPIView(generics.CreateAPIView):
	permission_classes = (permissions.AllowAny,)
	serializer_class = UserSerializer
	queryset = User.objects.all()

	def perform_create(self, serializer):
		password = serializer.validated_data.pop('password')
		serializer.save(password=make_password(password))



class UserLoginAPIView(JSONWebTokenAPIView):
    """
    API View that receives a POST with a user's username and password.

    Returns a JSON Web Token that can be used for authenticated requests.
    """
    serializer_class = UserJWTSerializer
    permission_classes = (permissions.AllowAny,)