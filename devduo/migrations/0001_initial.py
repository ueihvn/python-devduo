# Generated by Django 3.2.8 on 2021-11-28 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mentor_time', models.DateTimeField(null=True)),
                ('mentee_time', models.DateTimeField(null=True)),
                ('time_start', models.DateTimeField(auto_now_add=True, null=True)),
                ('duration', models.PositiveSmallIntegerField(null=True)),
                ('total_price', models.IntegerField(default=0)),
                ('status', models.CharField(choices=[('ongoing', 'Og'), ('finish', 'Fi'), ('cancel', 'Ca')], default='ongoing', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Field',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('image', models.URLField(null=True)),
                ('money', models.IntegerField(default=0)),
                ('user_name', models.CharField(max_length=5000, null=True)),
                ('gg_id', models.CharField(default='gg_id', max_length=5000, null=True)),
                ('password', models.CharField(default='1', max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=0)),
                ('comment', models.TextField(null=True)),
                ('booking', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='devduo.booking')),
            ],
        ),
        migrations.CreateModel(
            name='Mentor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=5000, null=True)),
                ('thumbnail', models.URLField(null=True)),
                ('contacts', models.JSONField(null=True)),
                ('description', models.TextField(max_length=5000, null=True)),
                ('price', models.IntegerField(default=0)),
                ('status', models.BooleanField(default=True)),
                ('fields', models.ManyToManyField(null=True, to='devduo.Field')),
                ('technologies', models.ManyToManyField(null=True, to='devduo.Technology')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='devduo.user')),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='mentee',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='devduo.user'),
        ),
        migrations.AddField(
            model_name='booking',
            name='mentor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='devduo.mentor'),
        ),
    ]
