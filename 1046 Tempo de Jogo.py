tempo = input().split()
inicial, final = tempo

inicial = int(tempo[0])
final = int(tempo[1])

if inicial < final :
    t = final - inicial
else :
    t = (24 - inicial) + final
print('O JOGO DUROU {} HORA(S)'.format(t))