import math

while True:

    tipo_calculadora = str(input('Qual tipo de calculadora deseja usar? (Simples ou Científica): '))
    num1 = float(input('Digite o número: '))

    if tipo_calculadora == 'Simples' or tipo_calculadora == 'simples':
        
        operacao_simples = str(input('Qual operação deseja fazer? (+, -, x, /): '))
        num2 = float(input('Digite o outro número: '))

        if operacao_simples == '+':
            result = num1 + num2 

        elif operacao_simples == '-':
            result = num1 - num2 

        elif operacao_simples == '/':
            if num2 == 0:
                print('ERRO: valor inválido para divisão por zero.')
            else:
                result = num1 / num2 

        elif operacao_simples == 'x':
            result = num1 * num2 

        print(f'{num1:.0f} {operacao_simples} {num2:.0f} = {result:.0f}')

    elif tipo_calculadora == 'Científica' or tipo_calculadora == 'científica' or tipo_calculadora == 'cientifica' or tipo_calculadora == 'Cientifica':

        operacao_cientifica = str(input('Qual operação deseja fazer? (Sen, Cos, Tan, Log, Potência, Raiz): '))

        if operacao_cientifica == 'Sen' or operacao_cientifica == 'sen':
            result = math.sin(math.radians(num1))
            print(f'{operacao_cientifica}({num1}) = {result}')

        elif operacao_cientifica == 'Cos' or operacao_cientifica == 'cos':
            result = math.cos(math.radians(num1))
            print(f'{operacao_cientifica}({num1}) = {result}')
        
        elif operacao_cientifica == 'Tan' or operacao_cientifica == 'tan':
            result = math.tan(math.radians(num1))
            print(f'{operacao_cientifica}({num1}) = {result}')

        elif operacao_cientifica == 'Log' or operacao_cientifica == 'log':
            result = math.log(math.radians(num1))
            print(f'{operacao_cientifica}({num1}) = {result}')
        
        elif operacao_cientifica == 'Potência' or operacao_cientifica == 'potência' or operacao_cientifica == 'Potencia' or operacao_cientifica == 'potencia':
            num2 = float(input('Digite o expoente:'))
            result = math.pow(num1,num2)
            print(f'{num1:.0f} elevado a {num2:.0f} = {result:.0f}')

        elif operacao_cientifica == 'Raiz' or operacao_cientifica == 'raiz':
            result = math.sqrt(num1)
            print(f'{operacao_cientifica}({num1}) = {result}')