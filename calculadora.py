import math

num1 = float(input('Digite o número: '))
tipo_calculadora = str(input('Qual tipo de calculadora deseja usar? (Simples ou Científica): '))
operacao_simples = str(input('Qual operação deseja fazer? (+, -, x, /): '))
num2 = float(input('Digite o outro número: '))

if tipo_calculadora == 'Simples' or tipo_calculadora == 'simples':
    if operacao_simples == '+':
        result = num1 + num2 

    if operacao_simples == '-':
        result = num1 - num2 

    if operacao_simples == '/':
        result = num1 / num2 

    if operacao_simples == 'x':
        result = num1 * num2 

    print(f'{num1:.0f} {operacao_simples} {num2:.0f} = {result:.0f}')

elif tipo_calculadora == 'Científica' or tipo_calculadora == 'científica' or tipo_calculadora == 'cientifica' or tipo_calculadora == 'Cientifica':
    pass