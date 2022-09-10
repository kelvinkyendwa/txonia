from django.shortcuts import render
from userFaker.models import FakeUser
from userFaker.serializers import FakeUserLoginSerializer, FakeUserSerializer

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *


@api_view(['GET', 'POST'])
def user_list(request):
    """
    List login and display user details.
    """
    if request.method == 'GET':
        users = FakeUser.objects.all()
        serializer = FakeUserSerializer
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = FakeUserLoginSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data2 = {
                'email': request.data['email'],
                'name': request.data['name'],
            }

            return Response(data2, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
