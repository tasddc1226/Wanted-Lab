# Generated by Django 4.0.4 on 2022-05-23 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_language_remove_company_company_en_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='language',
            name='code',
            field=models.CharField(max_length=2, unique=True),
        ),
    ]
