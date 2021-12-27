#달팽이는 올라가고 싶다
a,b,v = map(int, input().split())
v -= a
if v % (a-b) != 0:
    v = v // (a - b) +1
else:
    v = v // (a-b)
print(v + 1)
