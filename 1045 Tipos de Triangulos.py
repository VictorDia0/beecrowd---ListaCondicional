x = input().split()
a1,b2,c3 = x

a = float(1)
b = float(1)
c = float(1)
a1 = float(a1)
b2 = float(b2)
c3 = float(c3)

if a1 >= b2 and a1 >= c3 :
    a = a1
    if b2 >= c3:
        b = b2
        c = c3
    else:
        b = c3
        c = b2
if b2 >= a1 and b2 >= c3 :
    a = b2
    if a1 >= c3:
        b = a1
        c = c3
    else:
        b = c3
        c = a1
if c3 >= a1 and c3 >= b2 :
    a = c3
    if a1 >= b2:
        b = a1
        c = b2
    else:
        b = b2
        c = a1

if a == b and b == c:
    a = a1
    b = b2
    c = c3
a1 = a
b2 = b
c3 = c

if a >= (b + c) :
    print('NAO FORMA TRIANGULO')
else:
    if a**2 == (b**2 + c**2) :
        print('TRIANGULO RETANGULO')
    
    if (a**2 > (b**2) + (c**2)) :
        print('TRIANGULO OBTUSANGULO')
    
    if a**2 < (b**2) + (c**2) :
        print('TRIANGULO ACUTANGULO')
    
    if a == b and b == c :
        print('TRIANGULO EQUILATERO')
    
    if a == b != c or b == c != a or a == c != b:
        print('TRIANGULO ISOSCELES')