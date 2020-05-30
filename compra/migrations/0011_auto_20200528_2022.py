# Generated by Django 3.0.6 on 2020-05-29 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0010_auto_20200527_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compradetalle',
            name='precioCompra',
            field=models.FloatField(default=0, verbose_name='precioCompra'),
        ),
        migrations.AlterField(
            model_name='compradetalle',
            name='precioVenta',
            field=models.FloatField(default=0, verbose_name='precioVenta'),
        ),
        migrations.AlterField(
            model_name='compradetalle',
            name='subtotal',
            field=models.FloatField(default=0, verbose_name='subtotal'),
        ),
        migrations.AlterField(
            model_name='compradetalle',
            name='utilidad',
            field=models.FloatField(default=0, verbose_name='utilidad'),
        ),
    ]
