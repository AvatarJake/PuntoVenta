# Generated by Django 3.0.6 on 2020-05-28 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0002_auto_20200527_1837'),
        ('producto', '0008_auto_20200527_1743'),
        ('compra', '0009_compra_proveedor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compra',
            name='proveedor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='proveedores.Proveedor'),
        ),
        migrations.AlterField(
            model_name='compradetalle',
            name='compra',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='compra.Compra'),
        ),
        migrations.AlterField(
            model_name='compradetalle',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.Producto'),
        ),
    ]
