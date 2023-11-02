from django.urls import path
from . import views

app_name = 'trainingApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('calculate/', views.calculate, name='calculate'),
    path('calculate/', views.clear),
    path('dom/', views.run),
    path('radiobutton/', views.radiobutton),
    path('combobox/', views.combobox),
    path('computer/', views.choose_computer_model),
    path('raduga/<str:Color>', views.raduga, name="raduga"),
    path('raduga/', views.raduga, name="raduga"),
    path('radio_select/<str:Result>', views.radio_select, name="radio_select"),
    path('radio_select/', views.radio_select, name="radio_select"),
    path('checkbox/', views.sum_numbers),
    path('select/', views.select),
    path('select_combobox/', views.select),
    path('handle_dates/', views.handle_dates, name='handle_dates'),
]