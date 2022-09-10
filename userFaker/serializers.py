from userFaker.models import FakeUser
from rest_framework import serializers


class FakeUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = FakeUser
        fields = ('name', 'email')


class FakeUserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = FakeUser
        fields = '__all__'
