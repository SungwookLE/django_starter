# Generated by Django 2.1 on 2022-02-23 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('third', '0004_restaurant_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='image',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
    ]
