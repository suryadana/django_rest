from django.urls import path
from authentication.views import (
	UserCreateAPIView, UserLoginAPIView
)

urlpatterns = [
	path('auth/', UserLoginAPIView.as_view(), name="login"),
	path('auth/register/', UserCreateAPIView.as_view(), name='register')
]