# Generated by Django 3.2.6 on 2021-08-27 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptocoinersite', '0007_auto_20210827_1106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.CharField(max_length=200)),
            ],
        ),
    ]