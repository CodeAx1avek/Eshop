# Generated by Django 5.0 on 2024-02-03 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_order_approve_order_payment_id_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='payment_id',
        ),
    ]
