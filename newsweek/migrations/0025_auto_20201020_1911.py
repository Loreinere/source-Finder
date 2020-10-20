# Generated by Django 3.1.1 on 2020-10-20 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('newsweek', '0024_auto_20200929_1958'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsweek',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]