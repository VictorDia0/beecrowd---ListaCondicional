v1,v2,v3 = map(int,input().split())

if v1 > v2 and v1 > v3 :
    r1 = v1
    if v2 > v3 :
        r2 = v2
        r3 = v3
    else :
        r2 = v3
        r3 = v2
if v2 > v1 and v2 > v3:
    r1 = v2
    if v1 > v3:
        r2 = v1
        r3 = v3
    else:
        r2 = v3
        r3 = v1
if v3 > v1 and v3 > v2:
    r1 = v3
    if v1 > v2 :
        r2 = v1
        r3 = v2
    else:
        r3 = v1
        r2 = v2

print(r3)
print(r2)
print(r1)
print()
print(v1)
print(v2)
print(v3)