# Generated by Django 2.2.3 on 2019-08-24 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0009_auto_20190824_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='elevation_ft',
            field=models.SmallIntegerField(default=0),
        ),
    ]
