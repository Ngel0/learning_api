# Generated by Django 4.2.4 on 2023-09-09 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptodata', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cryptocurrency',
            name='volume_usd',
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='market_cap',
            field=models.DecimalField(decimal_places=5, max_digits=18),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='percent_change',
            field=models.DecimalField(decimal_places=8, max_digits=12),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='price',
            field=models.DecimalField(decimal_places=17, max_digits=23),
        ),
        migrations.AlterField(
            model_name='cryptocurrency',
            name='volume',
            field=models.DecimalField(decimal_places=8, max_digits=25),
        ),
    ]
