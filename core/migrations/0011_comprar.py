# Generated by Django 4.0.5 on 2022-07-14 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_producto_ids_alter_cliente_direccion_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='comprar',
            fields=[
                ('ids', models.CharField(max_length=1000, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=10)),
                ('asunto', models.CharField(max_length=50)),
                ('precio', models.CharField(max_length=20)),
            ],
        ),
    ]