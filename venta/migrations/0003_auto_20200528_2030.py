# Generated by Django 3.0.6 on 2020-05-29 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0002_auto_20200528_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ventadetalle',
            name='cantidad',
            field=models.PositiveIntegerField(default=0, verbose_name='cantidad'),
        ),
        migrations.AlterField(
            model_name='ventadetalle',
            name='precio',
            field=models.FloatField(default=0, verbose_name='precio'),
        ),
        migrations.AlterField(
            model_name='ventadetalle',
            name='subtotal',
            field=models.FloatField(default=0, verbose_name='subtotal'),
        ),
    ]