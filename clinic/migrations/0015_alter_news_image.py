# Generated by Django 4.2 on 2024-09-03 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0014_alter_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, default='news/default_icon.png', null=True, upload_to='news/'),
        ),
    ]