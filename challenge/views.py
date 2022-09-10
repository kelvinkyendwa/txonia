from django.contrib.auth.models import User
from serilizers import UserSerializer
from rest_framework import generics


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
