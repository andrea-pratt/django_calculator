from django.urls import path
from . import views


urlpatterns = [
                path('', views.calculator, name='calculator'),
                path('calculation/save/', views.save_calculation, name='save_calculation')
               ]
