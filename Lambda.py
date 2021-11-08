#1
L=lambda x:x+2
i=6
print(L(i))

#2
f=lambda z:z*11
i=9
print(f(i))

#3
f=lambda a,b:a*b
i,j=5,10
print(f(i,j))

#4
lst=[100, 10, 10000, 1, 9, 999, 99]
lst=sorted(lst,key=lambda x:100/x)
print(lst)
