# Generated by Django 3.2.2 on 2021-05-12 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocean', '0002_ukpostcodemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='amazonpricemodel',
            name='currency',
            field=models.CharField(default='GBP', max_length=3, verbose_name='currency'),
        ),
        migrations.AddField(
            model_name='cabinetitempricemodel',
            name='currency',
            field=models.CharField(default='GBP', max_length=3, verbose_name='currency'),
        ),
        migrations.AddField(
            model_name='fbaitempricemodel',
            name='currency',
            field=models.CharField(default='GBP', max_length=3, verbose_name='currency'),
        ),
        migrations.AddField(
            model_name='postcodepricemodel',
            name='currency',
            field=models.CharField(default='GBP', max_length=3, verbose_name='currency'),
        ),
        migrations.AddField(
            model_name='privateitempricemodel',
            name='currency',
            field=models.CharField(default='GBP', max_length=3, verbose_name='currency'),
        ),
    ]
