# Generated by Django 2.2.6 on 2019-11-14 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0005_auto_20191114_1602'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='producto',
            field=models.ManyToManyField(blank=True, through='ventas.ProductoVenta', to='ventas.Producto'),
        ),
    ]
