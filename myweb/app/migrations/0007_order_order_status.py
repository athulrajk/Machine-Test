# Generated by Django 4.1.7 on 2023-02-27 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_cart_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.BooleanField(default=True),
        ),
    ]
