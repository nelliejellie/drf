# Generated by Django 3.1.3 on 2020-12-13 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0009_auto_20201213_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='api_urls',
            name='how_to_use',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
