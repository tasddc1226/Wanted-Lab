# Generated by Django 4.0.4 on 2023-04-13 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_language_is_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='language',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
