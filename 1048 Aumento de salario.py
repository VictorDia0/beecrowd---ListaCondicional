salario = float(input())

if 0 < salario <= 400 :
    cal = salario * 1.15
    print(f'Novo salario: {cal:.2f}')
    print(f'Reajuste ganho: {salario * 0.15 :.2f}')
    print('Em percentual: 15 %')

elif 400.01 < salario <= 800 :
    cal = salario * 1.12
    print(f'Novo salario: {cal:.2f}')
    print(f'Reajuste ganho: {salario * 0.12 :.2f}')
    print('Em percentual: 12 %')
elif  800.01 <= salario <= 1200 :
    cal = salario * 1.10
    print(f'Novo salario: {cal:.2f}')
    print(f'Reajuste ganho: {salario * 0.10 :.2f}')
    print('Em percentual: 10 %')
elif 1200.01 <= salario <= 2000 :
    cal = salario * 1.07
    print(f'Novo salario: {cal:.2f}')
    print(f'Reajuste ganho: {salario * 0.07 :.2f}')
    print('Em percentual: 7 %')
elif salario > 2000 :
    cal = salario * 1.04
    print(f'Novo salario: {cal:.2f}')
    print(f'Reajuste ganho: {salario * 0.04 :.2f}')
    print('Em percentual: 4 %')