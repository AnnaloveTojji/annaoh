#덩치
a=int(input("몇명의 덩치를 비교할 건가요?"))
b=[]
for a in range(a):
    c,d=map(int,input("키와 몸무게를 한명씩 차례로 입력해주세요.").split())
    b.append((c,d))
for b in b:
    e=1
    for c in b:
        if b[0]<c[0] and b[1]<c[1]:
            f=e-1
        print(f)
