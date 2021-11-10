# Generated by Django 3.2.8 on 2021-11-09 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devduo', '0010_auto_20211108_1704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='fields',
            field=models.ManyToManyField(null=True, to='devduo.Field'),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='technologies',
            field=models.ManyToManyField(null=True, to='devduo.Technology'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_name',
            field=models.CharField(max_length=5000, null=True),
        ),
    ]