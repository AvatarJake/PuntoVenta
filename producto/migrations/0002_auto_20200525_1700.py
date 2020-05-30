# Generated by Django 3.0.6 on 2020-05-25 23:00

from django.db import migrations, models
import producto.models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='codigo',
            field=models.IntegerField(default=producto.models.Producto.number, editable=False, unique=True, verbose_name='codigo'),
        ),
    ]
