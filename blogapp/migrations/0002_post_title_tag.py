# Generated by Django 4.0.1 on 2022-01-16 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='My Awsome Blog!', max_length=255),
        ),
    ]
