# Generated by Django 4.0.5 on 2022-06-15 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_rename_clientes_cliente_rename_productos_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='ids',
            field=models.CharField(default=1, max_length=1000, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='rut',
            field=models.CharField(max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=10),
        ),
    ]
