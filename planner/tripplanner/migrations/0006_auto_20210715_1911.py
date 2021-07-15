# Generated by Django 3.2.5 on 2021-07-15 09:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tripplanner', '0005_auto_20210715_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='dest_city',
        ),
        migrations.AddField(
            model_name='trip',
            name='city_from',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='city_from', to='tripplanner.city'),
        ),
        migrations.AddField(
            model_name='trip',
            name='city_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='city_to', to='tripplanner.city'),
        ),
        migrations.AddField(
            model_name='trip',
            name='flight',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tripplanner.flight'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='airport_from',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='airport_from', to='tripplanner.city'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='airport_to',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='airport_to', to='tripplanner.city'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='trip',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='tripplanner.flight'),
        ),
    ]
