# Generated by Django 3.0.7 on 2020-06-26 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsweek', '0004_auto_20200626_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsweek',
            name='Title2',
            field=models.TextField(blank=True, null=True),
        ),
    ]