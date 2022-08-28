classe = str(input())
tipo = str(input())
classificacao = str(input())

if classe == 'vertebrado' :
    if tipo == 'ave':
        if classificacao == 'carnivoro' :
            print('aguia')
        if classificacao == 'onivoro' :
            print('pomba')
    if tipo == 'mamifero' :
        if classificacao == 'onivoro' :
            print('homem')
        if classificacao == 'herbivoro' :
            print('vaca')
if classe == 'invertebrado' :
    if tipo == 'inseto' :
        if classificacao == 'hematofago' :
            print('pulga')
        if classificacao == 'herbivoro' :
            print('lagarta')
    elif tipo == 'anelideo' :
        if classificacao == 'hematofago' :
            print('sanguessuga')
        if classificacao == 'onivoro' :
            print('minhoca')
        