# Generated by Django 3.0.7 on 2020-07-20 15:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newsweek', '0013_auto_20200720_1710'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsweek',
            name='author',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='newsweek',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='newsweek',
            name='slug',
            field=models.SlugField(max_length=250, null=True, unique_for_date='published'),
        ),
        migrations.AddField(
            model_name='newsweek',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
