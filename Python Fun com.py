#새로 시작한 강의 프로그램입니다.
#Python을 재미있게 배우는 장소 Python.Fun.com에 오신 것을 환영합니다.
#Python.Fun.com 에 들어오시면 이렇게 수업이 가능합니다.
#선생님 오주현 ♡~
#오늘은 백준 10부제 문제를 풀어보겠습니다.
#1강
x=int(input())
my_list=list(map(int,input().split()))
count=0
for i in my_list:
        if i==x:
                count=count+1
print(count)
