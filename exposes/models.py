from django.db import models

# Create your models here.
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from datetime import datetime


class Expose(models.Model):
    title = models.CharField(max_length=255)
    pdf = models.FileField(upload_to="pdf",blank=True)
    description = models.TextField(blank=True)
    date = models.DateTimeField(auto_now_add=True,blank=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return str(self.title) if self.title else ''

    def get_absolute_url(self):
        return reverse("expose_detail",args=[str(self.id)])