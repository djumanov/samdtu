# Generated by Django 4.2 on 2024-08-24 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0007_doc_doccategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='doc',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='clinic.doccategory'),
            preserve_default=False,
        ),
    ]