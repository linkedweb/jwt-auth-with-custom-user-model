from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
User = get_user_model()


class CreateUserAccount(APIView):
  permission_classes = [permissions.AllowAny, ]

  def post(self, request):
    data = request.data
    email = data['email']
    first_name = data['first_name']
    last_name = data['last_name']
    password = data['password']

    user = User.objects.filter(email=email)

    if user.exists():
      return Response(
        { 'error': 'User with this email already exists'}, 
        status=status.HTTP_400_BAD_REQUEST
      )

    User.objects.create_user(
      email=email, 
      first_name=first_name, 
      last_name=last_name, 
      password=password
    )

    return Response(
      { 'success': 'User created successfully' },
      status=status.HTTP_201_CREATED
    )


class RetrieveUserAccount(APIView):
  def get(self, request):
    user = request.user
    user = UserSerializer(user)

    return Response({ 'user': user.data }, status=status.HTTP_200_OK)
