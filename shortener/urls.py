from django.urls import path

from shortener.views import ShortenerCreateView, ShortenerRetrieveView

app_name = "shortener"

urlpatterns = [
    path("shortener/", ShortenerCreateView.as_view(), name="code-creation"),
    path("<str:short>/", ShortenerRetrieveView.as_view(), name="redirect"),
]
