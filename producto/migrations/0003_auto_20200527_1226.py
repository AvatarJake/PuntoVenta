# Generated by Django 3.0.6 on 2020-05-27 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0002_auto_20200525_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='existencias',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='producto',
            name='marca',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Marca'),
        ),
        migrations.AddField(
            model_name='producto',
            name='precio',
            field=models.FloatField(default=0),
        ),
    ]
