# Generated by Django 2.2 on 2020-03-05 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0005_auto_20200305_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='type_price',
            field=models.CharField(max_length=5),
        ),
    ]
