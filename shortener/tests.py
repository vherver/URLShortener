from rest_framework.test import APITestCase
from rest_framework import status
from unittest import TestCase

from shortener.models import URL
from shortener.serializers import URLSerializer


class ShortenerAPITestCase(APITestCase):
    def setUp(self):
        self.url = URL.objects.create(
            url="https://google.com",
        )

    def test_get_url(self):
        url = f"/{self.url.short}/"
        response = self.client.get(url)
        assert response.status_code == status.HTTP_200_OK
        assert response.json()["url"] == self.url.url

    def test_create_short_code_not_url_provided(self):
        url = "/shortener/"
        response = self.client.post(url)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data["url"][0].code == "required"

    def test_create_short_code(self):
        url = "/shortener/"
        data = {"url": "https://youtube.com"}
        response = self.client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json()["url"] == "https://youtube.com"


class TestURLSerializer(TestCase):
    def test_no_url_provided(self):
        data = {}
        serializer = URLSerializer(data=data)
        assert not serializer.is_valid()
        assert serializer.errors["url"][0].code == "required"

    def test_url_provided(self):
        data = {"url": "https://youtube.com"}
        assert URLSerializer(data=data).is_valid()

    def test_not_valid_url(self):
        data = {"url": "123"}
        serializer = URLSerializer(data=data)
        assert not serializer.is_valid()
        assert serializer.errors["url"][0].code == "invalid"
