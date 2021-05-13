from django.shortcuts import render
from time import sleep
from .models import Calculation


def calculator(request):

    sleep(.01) # allow time for ajax request to update database before query

    calculations = Calculation.objects.all().order_by('-id')[:10]

    return render(request, 'simple_calculator/calculator.html', {'calculations': calculations})


def save_calculation(request):

    first_operand = request.GET.get('first_operand')
    second_operand = request.GET.get('second_operand')
    result = request.GET.get('result')
    operator = request.GET.get('operator')
    calculation = f'{first_operand} {operator} {second_operand} = {result}'

    calculation = Calculation(calculation=str(calculation))
    calculation.save()

    calculations = Calculation.objects.all().order_by('-id')[:10]
    
    return render(request, 'simple_calculator/calculator.html', {'calculations': calculations})









