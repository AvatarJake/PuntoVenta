# Generated by Django 3.0.6 on 2020-05-28 00:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0001_initial'),
        ('compra', '0008_remove_compradetalle_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='compra',
            name='proveedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='proveedores.Proveedor'),
        ),
    ]
