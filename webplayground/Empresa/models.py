from django.db import models

class Empleado(models.Model):
    nombre = models.CharField(max_length=255, )
    apellido = models.CharField(max_length=255)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=10)
    direccion = models.CharField(max_length=255)
    telefono_contacto = models.CharField(max_length=15)
    correo_electronico = models.EmailField()
    fecha_contratacion = models.DateField()
    departamento = models.CharField(max_length=255)
    puesto = models.CharField(max_length=255)
    supervisor = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Horario(models.Model):
    DIA_CHOICES = [
        ('Lunes', 'Lunes'),
        ('Martes', 'Martes'),
        ('Miércoles', 'Miércoles'),
        ('Jueves', 'Jueves'),
        ('Viernes', 'Viernes'),
        ('Sábado', 'Sábado'),
        ('Domingo', 'Domingo'),
    ]

    dia_semana = models.CharField(max_length=20, choices=DIA_CHOICES)
    hora_inicio = models.TimeField()
    hora_finalizacion = models.TimeField()
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.dia_semana} {self.empleado.nombre}"

class Vacaciones(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha_inicio = models.DateField()
    fecha_finalizacion = models.DateField()
    estado_solicitud = models.CharField(max_length=20)
    motivo = models.TextField()
    
class Salario(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha_inicio_periodo = models.DateField()
    fecha_fin_periodo = models.DateField()
    salario_base = models.DecimalField(max_digits=10, decimal_places=2)
    bonificaciones = models.DecimalField(max_digits=10, decimal_places=2)
    deducciones = models.DecimalField(max_digits=10, decimal_places=2)
    total_pagar = models.DecimalField(max_digits=10, decimal_places=2)

class PagosCesantias(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    fecha_pago = models.DateField()
    valor_pagado = models.DecimalField(max_digits=10, decimal_places=2)
    periodo_correspondiente = models.CharField(max_length=20)

class RecursoHumano(models.Model):
    nombre_recurso = models.CharField(max_length=255)
    descripcion = models.TextField()
    contacto = models.CharField(max_length=255)
    departamento_perteneciente = models.CharField(max_length=255)
