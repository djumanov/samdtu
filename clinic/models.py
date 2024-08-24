from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Department(models.Model):
    picture = models.ImageField(
        upload_to='icons/', 
        default='icons/default_icon.png',
        blank=True, null=True
    )
    title = models.CharField(max_length=255)
    content = RichTextUploadingField()

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
    content = RichTextUploadingField()
    image = models.ImageField(
        upload_to='news/', 
        default='news/default_icon.png',
        blank=True, null=True
    )
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
    content = RichTextUploadingField()
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
    content = RichTextUploadingField()
    category = models.ForeignKey(DocCategory, on_delete=models.CASCADE)
    created = models.DateTimeField()

    def __str__(self):
        return self.title[:50]
    