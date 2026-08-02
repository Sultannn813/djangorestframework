from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer  

@api_view(['GET'])
def get_users(request): 
    return Response(UserSerializer({"name": "sultan", "age": 20}).data, status=status.HTTP_200_OK)

@api_view(['POST'])
def create_users(request):  # <-- Проверьте букву в букву
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
