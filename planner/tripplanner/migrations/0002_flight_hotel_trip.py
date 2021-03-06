# Generated by Django 3.2.5 on 2021-07-14 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tripplanner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airline', models.CharField(max_length=200)),
                ('airport_from', models.CharField(max_length=3)),
                ('airport_to', models.CharField(max_length=3)),
                ('boarding_time', models.DateTimeField(verbose_name='boarding time')),
                ('arrival_time', models.DateTimeField(verbose_name='arrival time')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dest_city', models.CharField(max_length=200)),
                ('start_date', models.DateTimeField(verbose_name='start date')),
                ('end_date', models.DateTimeField(verbose_name='end date')),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('url', models.URLField()),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tripplanner.flight')),
            ],
        ),
    ]
