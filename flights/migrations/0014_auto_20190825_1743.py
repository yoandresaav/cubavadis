# Generated by Django 2.2.3 on 2019-08-25 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0013_auto_20190825_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='airport',
            name='keywords',
            field=models.CharField(blank=True, max_length=320, null=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=340),
        ),
    ]
