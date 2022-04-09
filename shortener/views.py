from django.shortcuts import render
from rest_framework import generics, status

from shortener.serializers import URLSerializer


class ShortenerView(generics.CreateAPIView):
    serializer_class = URLSerializer



