# Generated by Django 3.0.6 on 2020-05-27 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compra', '0004_auto_20200527_0409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='compra',
            name='subtotal',
        ),
        migrations.AlterField(
            model_name='compradetalle',
            name='cantidad',
            field=models.PositiveIntegerField(default=0, verbose_name='cantidad'),
        ),
    ]