# Generated by Django 3.1.3 on 2020-12-11 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0002_auto_20201211_0730'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.CharField(choices=[('EndSraz', 'EndSarz'), ('Covid-19', 'Covid-19')], default='draft', max_length=10),
        ),
    ]
