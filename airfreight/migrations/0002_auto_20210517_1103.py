# Generated by Django 3.2.2 on 2021-05-17 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('airfreight', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='airfreightprice',
            name='receipt_area',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='op_airfreight_receipt', to='airfreight.airfreightreceiptlocal', verbose_name='receipt_area'),
        ),
        migrations.AlterField(
            model_name='airfreightprice',
            name='code',
            field=models.CharField(default='', max_length=5, verbose_name='code'),
        ),
        migrations.AlterUniqueTogether(
            name='airfreightprice',
            unique_together={('code', 'receipt_area')},
        ),
    ]