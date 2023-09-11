
from django import forms
from .models import Empleado, Horario, PagosCesantias, RecursoHumano, Salario, Vacaciones
#Empleado
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = '__all__'
        widgets = {
            'fecha_contratacion': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
            'fecha_nacimiento': forms.DateInput(format='%Y-%m-%d', attrs={'type': 'date'}),
        }
class EmpleadoSearchForm(forms.Form):
    search_term = forms.CharField(max_length=255, required=False, label='Buscar por Nombre o Apellido')

class HorarioForm(forms.ModelForm):
    class Meta:
        model = Horario
        fields = '__all__'
        widgets = {
            'hora_inicio': forms.TimeInput(attrs={'type': 'time'}),
            'hora_finalizacion': forms.TimeInput(attrs={'type': 'time'}),
        }

        
class SalarioForm(forms.ModelForm):
    class Meta:
        model = Salario
        fields = '__all__'
        widgets = {
            'fecha_inicio_periodo': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin_periodo': forms.DateInput(attrs={'type': 'date'}),
        }

class PagosCesantiasForm(forms.ModelForm):
    fecha_pago = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    valor_pagado = forms.DecimalField(
        max_digits=10, decimal_places=2, 
        widget=forms.TextInput(attrs={'type': 'number', 'step': '0.01'})
    )
    periodo_correspondiente = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = PagosCesantias
        fields = '__all__'
#
#
class RecursoHumanoForm(forms.ModelForm):
    class Meta:
        model = RecursoHumano
        fields = '__all__'

class VacacionesForm(forms.ModelForm):
    class Meta:
        model = Vacaciones
        fields = '__all__'
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'type': 'date'}),
            'fecha_finalizacion': forms.DateInput(attrs={'type': 'date'}),
            'estado_solicitud': forms.DateInput(attrs={'type': 'date'}),
        }

