# Generated by Django 3.0.6 on 2020-05-28 00:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proveedores', '0002_auto_20200527_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='correo',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='email'),
        ),
    ]
