# Generated by Django 4.1.4 on 2023-02-10 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminp', '0005_delete_coupon_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coupon',
            name='activ_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='exp_date',
            field=models.DateField(null=True),
        ),
    ]
