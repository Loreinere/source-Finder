# Generated by Django 3.0.7 on 2020-06-26 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsweek', '0002_auto_20200626_1856'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsweek',
            name='Issn',
            field=models.IntegerField(default=1),
        ),
    ]
