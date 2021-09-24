#직사각형에서 탈출
x,y,w,h=map(int,input().split())
a=w-x
b=h-y
c=x
d=y
print(min(a,b,c,d))
