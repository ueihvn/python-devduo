# Generated by Django 3.2.8 on 2021-10-18 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devduo', '0004_auto_20211018_0329'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='contact',
            field=models.JSONField(null=True),
        ),
    ]
