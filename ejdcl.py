#덩치
people=int(input("몇명의 키를 비교할건가요?"))
whole=[]
for i in range(people):
    weight,height=map(int,input("몸무게와 키를 차례로 입력하세요.(띄어쓰기 잊지 말고요!)").split())
    whole.append((weight,height))
for a in whole:
    rank=1
    for b in whole:
        if a[0]<b[0] and a[1]<b[1]:
            rank=rank-1
            
