from django.urls import path
from . import views

empleados_urlpatterns = [
    path('empleados/', views.empleado_list, name='empleado_list'),
    path('empleados/crear/', views.empleado_create, name='empleado_create'),
    path('empleados/editar/<int:pk>/', views.empleado_edit, name='empleado_edit'),
    path('empleados/eliminar/<int:pk>/', views.empleado_delete, name='empleado_delete'),
    path('horarios/', views.horario_list, name='horario_list'),
    path('horarios/nuevo/', views.horario_create, name='horario_create'),
    path('horarios/editar/<int:pk>/', views.horario_edit, name='horario_edit'),
    path('salarios/', views.salario_list, name='salario_list'),
    path('salarios/crear/', views.salario_create, name='salario_create'),
    path('salarios/editar/<int:pk>/', views.salario_edit, name='salario_edit'),
    path('salarios/eliminar/<int:pk>/', views.salario_delete, name='salario_delete'),
    path('pagoscesantias/', views.pago_list, name='pago_list'),
    path('pagoscesantias/nuevo/', views.pago_create, name='pago_create'),
    path('pagoscesantias/editar/<int:pk>/', views.pago_edit, name='pago_edit'),
    path('pagoscesantias/eliminar/<int:pk>/', views.pago_delete, name='pago_delete'),
    path('recurso/list/', views.recurso_list, name='recurso_list'),
    path('recurso/create/', views.recurso_create, name='recurso_create'),
    path('recurso/edit/<int:pk>/', views.recurso_edit, name='recurso_edit'),
    path('recurso/delete/<int:pk>/', views.recurso_delete, name='recurso_delete'),
    path('vacaciones/', views.vacaciones_list, name='vacaciones_list'),
    path('vacaciones/crear/', views.vacaciones_create, name='vacaciones_create'),
    path('vacaciones/editar/<int:pk>/', views.vacaciones_edit, name='vacaciones_edit'),
    path('generate_employee_report/<int:empleado_id>/', views.generate_employee_report, name='generate_employee_report'),
]

