# Generated by Django 4.2.7 on 2023-11-13 19:56

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='farm',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to=api.models.upload_to),
        ),
    ]