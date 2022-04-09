from django.urls import path

from shortener.views import ShortenerView

app_name = 'distributors_v1'

urlpatterns = [
    path("shortener/", ShortenerView.as_view(), name='Distributor List/ Creation'),
]