# Generated by Django 5.0.1 on 2024-04-17 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0008_alter_deliveryboy_adharnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='deliveryboy',
            name='is_registered',
            field=models.BooleanField(default=False),
        ),
    ]
