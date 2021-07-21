# Generated by Django 3.2.5 on 2021-07-21 11:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_post_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
    ]
