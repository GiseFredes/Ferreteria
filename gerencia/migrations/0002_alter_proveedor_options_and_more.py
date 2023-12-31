# Generated by Django 4.2.7 on 2023-11-17 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='proveedor',
            options={'verbose_name_plural': 'Proveedores'},
        ),
        migrations.RenameField(
            model_name='cliente',
            old_name='baja_cliente',
            new_name='baja',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='direccion_entrega',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='telefono_alternativo',
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(max_length=50, verbose_name='Teléfono'),
        ),
        migrations.AlterModelTable(
            name='detallepedido',
            table='Detalle de Pedido',
        ),
    ]
