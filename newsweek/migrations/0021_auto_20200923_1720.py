# Generated by Django 3.0.7 on 2020-09-23 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsweek', '0020_auto_20200923_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsweek',
            name='Points',
            field=models.IntegerField(default=1),
        ),
    ]