from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import User, Group, Entry
from .serializers import RegisterUserSerializer
from rest_framework.generics import ListAPIView, CreateAPIView


class RegisterUser(CreateAPIView):
    serializer_class = RegisterUserSerializer