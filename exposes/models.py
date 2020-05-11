from django.db import models

# Create your models here.
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


class Expose(models.Model):
    title = models.CharField(max_length=255)
    pdf = models.FileField(upload_to="pdf")
    description = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return str(self.title) if self.title else ''

    def get_absolute_url(self):
        return reverse("article_detail",args=[str(self.id)])