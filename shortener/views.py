from rest_framework import generics
from rest_framework.response import Response

from shortener.serializers import URLSerializer
from shortener.models import URL


class ShortenerCreateView(generics.CreateAPIView):
    serializer_class = URLSerializer


class ShortenerRetrieveView(generics.RetrieveAPIView):
    serializer_class = URLSerializer
    lookup_field = "short"
    queryset = URL.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.clicked()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
