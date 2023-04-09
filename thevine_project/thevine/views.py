from django.shortcuts import render
from .models import Wine, Rating, User
from rest_framework import generics
from .serializers import WineSerializer, RatingSerializer, UserSerializer

class WineList(generics.ListCreateAPIView):
    queryset = Wine.objects.all()
    serializer_class = WineSerializer

class WineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wine.objects.all()
    serializer_class = WineSerializer

class RatingList(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class RatingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer