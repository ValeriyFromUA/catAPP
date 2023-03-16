from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view
from rest_framework.response import Response

from catapp.models import UserManager


class UserCreateView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    permission_classes = [AllowAny]

    @api_view(['POST'])
    def create(self, request):
        email = request.data.get('email', None)
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        if email and username and password:
            user = UserManager().create_user(
                email=email,
                username=username,
                password=make_password(password),
            )
            return Response({'status': 'User created successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'error': 'Email, username, and password are required fields.'},
                            status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET'])
    def get(self, request):
        pass
