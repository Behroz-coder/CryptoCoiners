# Generated by Django 3.2.6 on 2021-08-31 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptocoinersite', '0010_auto_20210831_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='vote',
            field=models.IntegerField(default=0),
        ),
    ]
