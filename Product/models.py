from django.conf import settings
from django.db import models
from django.utils import timezone


class Product(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    weight = models.TextField(max_length=15)
    price = models.TextField(max_length=15)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.updated_at = timezone.now()
        self.created_at = timezone.now()
        self.save()

    def __str__(self):
        return self.title