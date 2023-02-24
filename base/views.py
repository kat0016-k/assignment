from rest_framework import generics, filters, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Client, Artist, Work
from .serializers import ClientSerializer, ArtistSerializer, WorkSerializer, UserSerializer
from .filters import ArtistFilter, WorkFilter
from django_filters.rest_framework import DjangoFilterBackend

class WorkList(generics.ListCreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = WorkFilter

class ArtistList(generics.ListAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ArtistFilter



@api_view(['POST'])
def register(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        login(request, user)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
