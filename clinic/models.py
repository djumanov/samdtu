from django.db import models


class MenuItem(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title


class SubMenuItem(models.Model):
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100, blank=True, null=True)
    menu_item = models.ForeignKey(MenuItem, related_name='submenus', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
