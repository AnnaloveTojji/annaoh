#문자열 반복
#11-w-d-g-o
a=int(input("반복"))
c=input("단어")
b=list(c)
x=len(b)
for i in range(x):
    y=b[i]*a
    print(y,end="")
