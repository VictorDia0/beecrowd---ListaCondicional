multiplos = input().split()

x, y = multiplos

x = int(x)
y = int(y)

if x > y :
    if x % y == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
elif y > x :
    if y % x == 0:
        print('Sao Multiplos')
    else:
        print('Nao sao Multiplos')
elif x == y:
    print('Sao Multiplos')