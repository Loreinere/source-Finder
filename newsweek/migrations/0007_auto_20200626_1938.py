# Generated by Django 3.0.7 on 2020-06-26 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsweek', '0006_newsweek_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsweek',
            name='architecture and urbanistic',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='newsweek',
            name='history',
            field=models.TextField(null=True),
        ),
    ]
