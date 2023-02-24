from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Client, Artist, Work


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'


class ArtistSerializer(serializers.ModelSerializer):
    works = WorkSerializer(many=True)

    class Meta:
        model = Artist
        fields = ['id', 'name', 'works']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(username=validated_data['username'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'password']