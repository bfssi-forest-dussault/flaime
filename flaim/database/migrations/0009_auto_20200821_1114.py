# Generated by Django 3.0.7 on 2020-08-21 15:14

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0008_auto_20200817_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalproduct',
            name='upc_array',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=500), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='product',
            name='upc_array',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=500), blank=True, null=True, size=None),
        ),
    ]