# Generated by Django 3.2.5 on 2021-08-17 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('icon', '0009_womancomment_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='womancomment',
            name='is_liked',
            field=models.BooleanField(default=False),
        ),
    ]
