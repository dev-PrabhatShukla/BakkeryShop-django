# Generated by Django 3.1 on 2021-05-07 19:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_auto_20210508_0032'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='quality',
            new_name='quantity',
        ),
    ]
