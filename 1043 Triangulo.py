tri = input().split()

a,b,c = tri

a = float(a)
b = float(b)
c = float(c)

area = ((a + b) * c)/2
perimetro = a + b + c

if a < (b + c) and b < (a + c) and c < (a + b) :
    print(f'Perimetro = {perimetro:.1f}')
else:
    print(f'Area = {area:.1f}')