# Generated by Django 3.0.6 on 2020-05-25 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TotalCompra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='compradetalle',
            name='precioCompra',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Precio de Compra Unitario'),
        ),
        migrations.AlterField(
            model_name='compradetalle',
            name='precioVenta',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Precio Venta Unitario'),
        ),
    ]
