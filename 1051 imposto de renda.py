salario = float(input())
if 0 < salario <= 2000 :
    print('Isento')
else:
    if 2000.01 <= salario <= 3000 :
        cal = salario - 2000
        imposto = cal * 0.08
    if 3000.01 <= salario <= 4500 :
        cal = salario - 3000
        imposto = (0.08 * 1000) + (cal * 0.18)
    if salario > 4500 :
        cal = salario - 4500
        imposto = (0.08 * 1000) + (0.18 * 1500) + (cal * 0.28)

    print(f'R$ {imposto:.2f}')