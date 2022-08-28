intervalo = float(input())
if 0 <= intervalo <= 25 :
    print('Intervalo [0,25]')
if 25 < intervalo <= 50 :
    print('Intervalo (25,50]')
if 50 < intervalo <= 75 :
    print('Intervalo (50,75]')
if 75 < intervalo <= 100 :
    print('Intervalo (75,100]')
if intervalo > 100 or intervalo < 0 :
    print('Fora de intervalo')