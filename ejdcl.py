#덩치
a=int(input("몇명의 덩치를 비교할 건가요?"))
b=[]
for c in range(a):
    d,e=map(int,input("몸무게와 키를 한명씩 차례로 입력해주세요.").split())
    b.append((d,e))
for f in b:
    g=1
    for h in b:
        if f[0]<h[0] and f[1]<h[1]:
            g=g+1
    print(g,end='')
