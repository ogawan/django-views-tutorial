# Generated by Django 3.0.5 on 2020-04-21 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_views', '0003_auto_20200420_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='facebook_profile',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='instagram_profile',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='twitter_profile',
            field=models.URLField(null=True),
        ),
    ]
