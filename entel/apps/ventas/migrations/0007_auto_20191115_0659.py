# Generated by Django 2.2.6 on 2019-11-15 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0006_venta_producto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productoventa',
            name='cantidad',
            field=models.IntegerField(null=True),
        ),
    ]