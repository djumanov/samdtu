from django.db import models
# from ckeditor_uploader.fields import RichTextUploadingField
from .validators import validate_image_size
from django.conf import settings
from urllib.parse import urljoin


class Department(models.Model):
    picture = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title[:50]


class NewsCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class News(models.Model):
    keywords = models.CharField(max_length=256)
    description = models.CharField(max_length=150)
    title = models.CharField(max_length=256)
    content = models.TextField()
    image = models.CharField(max_length=255, blank=True, null=True)
    images = models.TextField(blank=True, null=True)
    created = models.DateTimeField()
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    alias = models.CharField(max_length=256, unique=True)
    published = models.BooleanField(default=False)
    viewers = models.PositiveIntegerField(default=1294)

    def __str__(self):
        return self.title[:50]


class Info(models.Model):
    keywords = models.CharField(max_length=256)
    description = models.CharField(max_length=150)
    title = models.CharField(max_length=256)
    content = models.TextField()
    alias = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.title[:50]


class DocCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Doc(models.Model):
    title = models.CharField(max_length=256)
    doc = models.FileField(upload_to='docs/', blank=True, null=True)
    content = models.TextField()
    category = models.ForeignKey(DocCategory, on_delete=models.CASCADE)
    created = models.DateTimeField()

    def __str__(self):
        return self.title[:50]
    

class Image(models.Model):
    image = models.ImageField(upload_to='images/', validators=[validate_image_size])

    def __str__(self):
        return self.image.url
    