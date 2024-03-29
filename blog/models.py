from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

from django.utils.timezone import now

from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    summary = models.CharField(max_length=100, default="")
    body = RichTextUploadingField()
    tags = models.ManyToManyField("Tag")

    date_of_creation = models.DateTimeField(auto_now_add=True)
    date_of_last_update = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.title} • by {self.author}"

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True, default=None)
    colour = models.CharField(max_length=7, default="#888888")

    def __str__(self) -> str:
        return f"{self.name} • {self.colour}"
