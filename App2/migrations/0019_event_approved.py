# Generated by Django 4.0.5 on 2022-07-25 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App2', '0018_event_overseer'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]