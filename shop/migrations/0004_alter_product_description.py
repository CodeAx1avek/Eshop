# Generated by Django 4.2.1 on 2023-05-29 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(default='Best Qualtiy', max_length=200),
        ),
    ]
