# Generated by Django 3.2.8 on 2021-11-10 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('devduo', '0016_alter_booking_time_start'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mentor',
            old_name='thumnail',
            new_name='thumbnail',
        ),
    ]
