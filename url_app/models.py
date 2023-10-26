from django.db import models
from django.utils.crypto import get_random_string

class ShortenedURL(models.Model):
    id = models.AutoField(primary_key=True)
    original_url = models.URLField(unique=True)
    short_url = models.CharField(max_length=10, unique=True)

    def save(self, *args, **kwargs):
        # Kısaltılmış URL oluştur
        if not self.short_url:
            self.short_url = get_random_string(length=8)
        super().save(*args, **kwargs)
