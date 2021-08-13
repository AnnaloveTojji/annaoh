#1단계: 해킹을 한다.
#2단계: 정답을 빼낸다.
numbers=int(input("너까지 포함한 너의 반 명수를 입력해줘"))
mylist=list(map(int,input("너의 점수를 가장 앞에 쓰고 나머지 점수를 뒤에 입력해줘").split()))
sum=0
for i in mylist:
    sum=sum+i
p=sum/numbers
m=mylist[0]
if p<m:
    print("너의 점수는 평균보다 높아")
elif m<p:
    print("너의 점수는 평균보다 낮아")
else:
    print("너의 점수는 평균이야")

    
