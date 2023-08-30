# Generated by Django 4.1.7 on 2023-02-28 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Shipped', 'Shipped'), ('Packed', 'Packed'), ('New', 'New')], default='New', max_length=20),
        ),
    ]
