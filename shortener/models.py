import time

from hashlib import md5
from django.db import models


class URL(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    url = models.URLField()
    short = models.CharField(max_length=10, unique=True)
    clicks = models.PositiveIntegerField(default=0)

    def clicked(self):
        self.clicks += 1
        self.save(update_fields=["clicks"])

    def save(self, *args, **kwargs):
        if not self.id:
            self.short = md5(f"{self.url}{time.time()}".encode()).hexdigest()[:10]

        return super().save(*args, **kwargs)

    def __str__(self):
        return self.url
