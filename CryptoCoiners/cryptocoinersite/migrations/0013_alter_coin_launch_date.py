# Generated by Django 3.2.6 on 2021-08-31 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptocoinersite', '0012_alter_coin_launch_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='launch_date',
            field=models.DateField(verbose_name=''),
        ),
    ]