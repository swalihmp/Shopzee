# Generated by Django 4.1.4 on 2023-02-10 06:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('store', '0013_alter_variation_variation_category'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='review',
            new_name='Review_Rating',
        ),
    ]