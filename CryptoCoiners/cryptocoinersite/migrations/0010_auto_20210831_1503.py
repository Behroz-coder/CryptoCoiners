# Generated by Django 3.2.6 on 2021-08-31 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptocoinersite', '0009_coin_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='coin_dis',
            field=models.CharField(default=1, max_length=800),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coin',
            name='coin_id',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
