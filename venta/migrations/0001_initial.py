# Generated by Django 3.0.6 on 2020-05-27 22:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('producto', '0007_auto_20200527_1352'),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaVenta', models.DateField(blank=True, null=True, verbose_name='Fecha de Compra')),
                ('noFactura', models.CharField(max_length=100, null=True)),
                ('total', models.FloatField(default=0.0)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='VentaDetalle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=0, verbose_name='cantidad')),
                ('precio', models.FloatField(default=0)),
                ('subtotal', models.FloatField(default=0)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producto.Producto')),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='venta.Venta')),
            ],
        ),
    ]
