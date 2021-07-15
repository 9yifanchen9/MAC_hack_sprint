# Generated by Django 3.2.5 on 2021-07-15 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tripplanner', '0004_merge_0003_auto_20210714_2134_0003_auto_20210715_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(default='', max_length=3)),
            ],
        ),
        migrations.AlterField(
            model_name='hotel',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tripplanner.flight'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='airport_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='airport_from', to='tripplanner.city'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='airport_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='airport_to', to='tripplanner.city'),
        ),
    ]
