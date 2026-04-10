num1 = float(input('Digite o número: '))
operacao = str(input('Qual operação deseja fazer? (+. -, x, /): '))
num2 = float(input('Digite o outro número: '))

if operacao== '+':
    result = num1 + num2 

if operacao== '-':
    result = num1 - num2 

if operacao== '/':
    result = num1 / num2 

if operacao== 'x':
    result = num1 * num2 

print(f'{num1:.0f} {operacao} {num2:.0f} = {result:.0f}')