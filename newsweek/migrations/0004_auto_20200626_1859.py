# Generated by Django 3.0.7 on 2020-06-26 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsweek', '0003_newsweek_issn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsweek',
            name='Issn',
            field=models.TextField(),
        ),
    ]