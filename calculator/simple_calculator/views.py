from django.shortcuts import render
from time import sleep
from .models import Calculation
import os


def calculator(request):

    sleep(0.01) # allow time for ajax request to update database before query

    calculations = Calculation.objects.all().order_by('-creation_date')[:10]

    return render(request, 'simple_calculator/calculator.html', {'calculations': calculations})


def save_calculation(request):

    if request.method == 'POST':
        first_operand = request.POST.get('first_operand')
        second_operand = request.POST.get('second_operand')
        result = request.POST.get('result')
        operator = request.POST.get('operator')
        calculation = f'{first_operand} {operator} {second_operand} = {result}'

        calculation = Calculation(calculation=calculation)
        calculation.save()

        calculations = Calculation.objects.all().order_by('-creation_date')[:10]
    
    return render(request, 'simple_calculator/calculator.html', {'calculations': calculations})









