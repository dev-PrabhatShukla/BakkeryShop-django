# Generated by Django 3.1 on 2021-05-07 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210506_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='delivery_charge',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
