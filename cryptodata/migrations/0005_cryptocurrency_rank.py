# Generated by Django 4.2.4 on 2023-10-03 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cryptodata', '0004_alter_cryptocurrency_percent_change_1h_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cryptocurrency',
            name='rank',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
