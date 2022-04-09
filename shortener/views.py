from rest_framework import generics

from shortener.serializers import URLSerializer
from shortener.models import URL


class ShortenerCreateView(generics.CreateAPIView):
    serializer_class = URLSerializer


class ShortenerRetrieveView(generics.RetrieveAPIView):
    serializer_class = URLSerializer
    lookup_field = "short"
    queryset = URL.objects.all()
