# Generated by Django 4.2.1 on 2023-08-04 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_order_address_order_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
