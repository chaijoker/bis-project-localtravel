# Generated by Django 2.2 on 2020-04-19 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0008_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='image_pay',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
