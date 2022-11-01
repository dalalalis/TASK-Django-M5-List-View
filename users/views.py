from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from .serializers import UserCreateSerializer
# Create your views here.
class UserCreateAPIview(CreateAPIView):
    serializer_class=UserCreateSerializer