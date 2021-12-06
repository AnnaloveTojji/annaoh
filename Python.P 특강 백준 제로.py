#Python.P 강의에 오신 것을 환영합니다.
#1강부터 5강까지 진행될 예정이며 Python을 배우는 공간입니다.
#1강
#선생님:오주현 ♡
#백준 제로 문제를 풀어봅시다.
k=int(input("정수 k를 입력해 주세요."))
my_list=[]
for i in range(k):
     n=int(input("정수 n을 입력해 주세요."))
     if n==0:
          my_list.pop()
     else:
          my_list.append(n)
print(sum(my_list))
