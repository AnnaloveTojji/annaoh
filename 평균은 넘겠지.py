#평균은 넘겠지
print("만약 '입력해'라는 창이 나온다면 첫번째로 반 학생의 수를 입력해. 그런데 이 때 너도 포함 해야 해. 그리고 띄어쓰기를 하고 그 뒤로 너희 반 학생들의 점수를 다 입력해줘. 중요한 것은 점수를 입력할 때도 점수와 점수 사이에 띄어쓰기가 꼭 있어야 해! 그럼 이제 할 수 있겠지?")
score=list(map(int,input("입력해").split()))
x=score[0]
y=sum(score)-x
z=y/x
count=0
for i in score[1:]:
    if i>z:
        count=count+1
a=count/x*100
print(a)
    
