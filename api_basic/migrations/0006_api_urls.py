# Generated by Django 3.1.3 on 2020-12-13 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0005_auto_20201211_0856'),
    ]

    operations = [
        migrations.CreateModel(
            name='Api_Urls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(max_length=30)),
            ],
        ),
    ]