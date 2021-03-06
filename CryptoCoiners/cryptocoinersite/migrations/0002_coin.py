# Generated by Django 3.2.6 on 2021-08-25 15:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cryptocoinersite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='coin',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('coin_name', models.CharField(max_length=200)),
                ('coin_symbol', models.CharField(max_length=200)),
                ('coin_discription', models.CharField(max_length=800)),
                ('market_cap', models.IntegerField()),
                ('price', models.IntegerField()),
                ('launch_date', models.DateTimeField(verbose_name='')),
                ('website', models.CharField(max_length=200)),
                ('telegram', models.CharField(max_length=200)),
                ('twitter', models.CharField(max_length=200)),
                ('discord', models.CharField(max_length=200)),
                ('reddit', models.CharField(max_length=200)),
                ('logo', models.CharField(max_length=200)),
                ('additional_info', models.CharField(max_length=800)),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('class_type', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
