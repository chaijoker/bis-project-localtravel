# Generated by Django 2.2 on 2020-03-05 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0004_trip_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='price_trip',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='trip',
            name='type_price',
            field=models.FloatField(default=2),
            preserve_default=False,
        ),
    ]