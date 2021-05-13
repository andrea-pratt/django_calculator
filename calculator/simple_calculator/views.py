from django.shortcuts import render
from time import sleep
from .models import Calculation
import os


def calculator(request):

    sleep(.01) # allow time for ajax request to update database before query

    calculation = Calculation(calculation='test string')
    calculation.save()


    calculations = Calculation.objects.all().order_by('-id')[:10]

    return render(request, 'simple_calculator/calculator.html', {'calculations': calculations})


def save_calculation(request):

    calculation = Calculation(calculation='test string from save_calculation')
    calculation.save()

    calculations = ['hello', 'hi']


    first_operand = request.GET.get('first_operand')
    second_operand = request.GET.get('second_operand')
    result = request.GET.get('result')
    operator = request.GET.get('operator')
    calculation = f'{first_operand} {operator} {second_operand} = {result}'

    calculation = Calculation(calculation=calculation)
    calculation = Calculation(calculation='test string from save_calculation')
    calculation.save()

    calculations = Calculation.objects.all().order_by('-id')[:10]
    
    return render(request, 'simple_calculator/calculator.html', {'calculations': calculations})









