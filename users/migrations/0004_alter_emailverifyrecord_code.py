# Generated by Django 3.2.2 on 2021-05-12 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_emailverifyrecord_is_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='code',
            field=models.CharField(max_length=30, verbose_name='Verify Code'),
        ),
    ]
