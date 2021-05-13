from django.shortcuts import render
from time import sleep
import os


def calculator(request):

    sleep(0.01) # allow time for ajax request to update database before query

    calculations = get_last_10_calculations()

    return render(request, 'simple_calculator/calculator.html', {'calculations': calculations})


def save_calculation(request):

    if request.method == 'POST':
        first_operand = request.POST.get('first_operand')
        second_operand = request.POST.get('second_operand')
        result = request.POST.get('result')
        operator = request.POST.get('operator')
        calculation = f'{first_operand} {operator} {second_operand} = {result}'

        write_calculation(calculation)
        calculations = get_last_10_calculations()
    
    return render(request, 'simple_calculator/calculator.html', {'calculations': calculations})


def get_last_10_calculations():

    working_directory = os.getcwd()
    filename = os.path.join(working_directory, 'simple_calculator', 'calculations.txt')

    with open(filename, 'r') as calc_file:
        lines = calc_file.readlines()

    calculations = []
 
    for i in range(10):
        try:
            calculations.append(lines[i*-1])
        except IndexError:
            break

    return calculations


def write_calculation(calculation):

    working_directory = os.getcwd()
    filename = os.path.join(working_directory, 'simple_calculator', 'calculations.txt')

    with open(filename, 'a') as calc_file:
        calc_file.write(calculation + '\n')






