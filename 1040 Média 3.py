x = input().split()
n1,n2,n3,n4 = x

n1 = float(n1) * 2
n2 = float(n2) * 3
n3 = float(n3) * 4
n4 = float(n4) * 1
media = (n1+n2+n3+n4)/10

print(f'Media: {media:.1f}')

if media >= 7.0 :
    print('Aluno aprovado.')
elif media < 5.0 :
    print('Aluno reprovado.')
elif media >= 5.0 and media <= 6.9 :
    print('Aluno em exame.')
    exame = float(input())
    print(f'Nota do exame: {exame:.1f}')
    media2 = (exame + media) / 2
    if media2 >= 5 :
        print('Aluno aprovado.')
        print(f'Media final: {media2:.1f}')
    else :
        print('Aluno reprovado.')
        print(f'Media final: {media2:.1f}')