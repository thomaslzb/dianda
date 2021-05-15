# Generated by Django 3.2.2 on 2021-05-12 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AirfreightReceiptLocal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(default='', max_length=10, unique=True, verbose_name='city')),
                ('op_last_update', models.DateTimeField(auto_now=True, verbose_name='Operate Datetime')),
                ('op_user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='op_air_receipt_local', to=settings.AUTH_USER_MODEL, verbose_name='Operator')),
            ],
            options={
                'verbose_name': 'airfreight_receipt_local',
                'db_table': 'airfreight_receipt_local',
                'ordering': ['city'],
            },
        ),
        migrations.CreateModel(
            name='AirfreightPrice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(default='', max_length=5, unique=True, verbose_name='code')),
                ('en_name', models.CharField(default='', max_length=50, verbose_name='en_name')),
                ('cn_name', models.CharField(default='', max_length=50, verbose_name='cn_name')),
                ('currency', models.CharField(default='RMB', max_length=3, verbose_name='currency')),
                ('min_weight', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, verbose_name='min_weight')),
                ('max_weight', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, verbose_name='max_weight')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, verbose_name='price')),
                ('fee_type', models.IntegerField(default='0', verbose_name='fee_type')),
                ('remark', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='remark')),
                ('op_last_update', models.DateTimeField(auto_now=True, verbose_name='Operate Datetime')),
                ('op_user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='op_airfreight_price', to=settings.AUTH_USER_MODEL, verbose_name='Operator')),
            ],
            options={
                'verbose_name': 'airfreight_price',
                'db_table': 'airfreight_price',
                'ordering': ['code'],
            },
        ),
        migrations.CreateModel(
            name='AirfreightPostcodeType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type_name', models.CharField(default='', max_length=50, unique=True, verbose_name='en_name')),
                ('currency', models.CharField(default='RMB', max_length=3, verbose_name='currency')),
                ('price', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, verbose_name='price')),
                ('op_last_update', models.DateTimeField(auto_now=True, verbose_name='Operate Datetime')),
                ('op_user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='op_air_postcode_type', to=settings.AUTH_USER_MODEL, verbose_name='Operator')),
            ],
            options={
                'verbose_name': 'airfreight_postcode_price',
                'db_table': 'airfreight_postcode_price',
                'ordering': ['type_name'],
            },
        ),
        migrations.CreateModel(
            name='AirfreightPostcode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('begin_code', models.CharField(default='', max_length=10, unique=True, verbose_name='begin_code')),
                ('end_code', models.CharField(default='', max_length=10, verbose_name='end_code')),
                ('op_last_update', models.DateTimeField(auto_now=True, verbose_name='Operate Datetime')),
                ('op_user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='op_air_postcode_detail', to=settings.AUTH_USER_MODEL, verbose_name='Operator')),
                ('postcode_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='airfreight.airfreightpostcodetype', verbose_name='postcode_type')),
            ],
            options={
                'verbose_name': 'ocean_postcode_detail',
                'db_table': 'airfreight_postcode_detail',
                'ordering': ['postcode_type', 'begin_code'],
            },
        ),
        migrations.CreateModel(
            name='AirfreightItemPrice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fee_code', models.CharField(default='', max_length=5, unique=True, verbose_name='fee_code')),
                ('en_name', models.CharField(default='', max_length=50, verbose_name='en_name')),
                ('cn_name', models.CharField(default='', max_length=50, verbose_name='cn_name')),
                ('unit', models.CharField(default='', max_length=20, verbose_name='unit')),
                ('rate', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, verbose_name='rate')),
                ('currency', models.CharField(default='RMB', max_length=3, verbose_name='currency')),
                ('minimum_charge', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=8, verbose_name='minimum_charge')),
                ('fee_type', models.IntegerField(default='0', verbose_name='fee_type')),
                ('remark', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='remark')),
                ('op_last_update', models.DateTimeField(auto_now=True, verbose_name='Operate Datetime')),
                ('op_user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='op_airfreight_item_price', to=settings.AUTH_USER_MODEL, verbose_name='Operator')),
            ],
            options={
                'verbose_name': 'airfreight_item_price',
                'db_table': 'airfreight_item_price',
                'ordering': ['en_name'],
            },
        ),
    ]
