# Generated by Django 3.0.6 on 2020-05-27 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0005_auto_20200527_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compradetalle',
            name='total',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
