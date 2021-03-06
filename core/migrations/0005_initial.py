# Generated by Django 4.0.4 on 2022-06-10 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0004_delete_contacto_delete_registroo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=10, verbose_name='Nombre')),
                ('Apellido', models.CharField(max_length=10, verbose_name='Apellido')),
                ('Email', models.CharField(max_length=20, verbose_name='E-mail')),
                ('Asunto', models.CharField(max_length=9, verbose_name='Asunto')),
                ('Asunto2', models.CharField(max_length=20, verbose_name='Asunto2')),
            ],
        ),
        migrations.CreateModel(
            name='Registroo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=6, verbose_name='Nombre')),
                ('Edad', models.CharField(max_length=2, verbose_name='Edad')),
                ('Email', models.CharField(max_length=20, verbose_name='E-mail')),
                ('Telefono', models.CharField(max_length=9, verbose_name='Telefono')),
                ('Contraseña', models.CharField(max_length=20, verbose_name='Contraseña')),
            ],
        ),
    ]
