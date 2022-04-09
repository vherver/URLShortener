from rest_framework import serializers

from shortener.models import URL


class URLSerializer(serializers.ModelSerializer):

    short = serializers.CharField(read_only=True)

    class Meta:
        model = URL
        fields = ("url", "short")
