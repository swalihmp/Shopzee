# Generated by Django 4.1.4 on 2023-02-10 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_rename_review_review_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_category',
            field=models.CharField(choices=[('color', 'color'), ('size', 'size')], max_length=100),
        ),
    ]