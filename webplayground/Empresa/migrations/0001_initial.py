# Generated by Django 4.0.2 on 2023-09-01 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('apellido', models.CharField(max_length=255)),
                ('fecha_nacimiento', models.DateField()),
                ('genero', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=255)),
                ('telefono_contacto', models.CharField(max_length=15)),
                ('correo_electronico', models.EmailField(max_length=254)),
                ('fecha_contratacion', models.DateField()),
                ('departamento', models.CharField(max_length=255)),
                ('puesto', models.CharField(max_length=255)),
                ('supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Empresa.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='RecursoHumano',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_recurso', models.CharField(max_length=255)),
                ('descripcion', models.TextField()),
                ('contacto', models.CharField(max_length=255)),
                ('departamento_perteneciente', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Vacaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('fecha_finalizacion', models.DateField()),
                ('estado_solicitud', models.CharField(max_length=20)),
                ('motivo', models.TextField()),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empresa.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Salario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio_periodo', models.DateField()),
                ('fecha_fin_periodo', models.DateField()),
                ('salario_base', models.DecimalField(decimal_places=2, max_digits=10)),
                ('bonificaciones', models.DecimalField(decimal_places=2, max_digits=10)),
                ('deducciones', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_pagar', models.DecimalField(decimal_places=2, max_digits=10)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empresa.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='PagosCesantias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pago', models.DateField()),
                ('valor_pagado', models.DecimalField(decimal_places=2, max_digits=10)),
                ('periodo_correspondiente', models.CharField(max_length=20)),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empresa.empleado')),
            ],
        ),
        migrations.CreateModel(
            name='Horario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_semana', models.CharField(max_length=20)),
                ('hora_inicio', models.TimeField()),
                ('hora_finalizacion', models.TimeField()),
                ('empleado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Empresa.empleado')),
            ],
        ),
    ]
