# Generated by Django 3.1 on 2021-05-19 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20210519_0151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variation',
            name='variation_value',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]