# Generated by Django 3.0.7 on 2020-07-16 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsweek', '0007_auto_20200626_1938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsweek',
            old_name='Title1',
            new_name='Title',
        ),
        migrations.RemoveField(
            model_name='newsweek',
            name='Title2',
        ),
        migrations.AddField(
            model_name='newsweek',
            name='Second Title',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
    ]
