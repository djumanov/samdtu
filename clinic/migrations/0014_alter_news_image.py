# Generated by Django 4.2 on 2024-09-03 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0013_alter_department_content_alter_department_content_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]