# Generated by Django 2.0.3 on 2018-04-10 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20180404_2141'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
