# Generated by Django 3.1.3 on 2020-12-11 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_basic', '0003_article_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='categories',
            field=models.CharField(choices=[('not selected', 'not selected'), ('EndSraz', 'EndSarz'), ('Covid-19', 'Covid-19')], default='not selected', max_length=30),
        ),
        migrations.AlterField(
            model_name='article',
            name='quote',
            field=models.TextField(max_length=500),
        ),
    ]