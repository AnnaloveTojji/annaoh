#Python.P 강의에 오신 것을 환영합니다.
#1강부터 5강까지 진행될 예정이며 Python을 배우는 공간입니다.
#2강
#선생님:오주현 ♡
#백준 괄호 문제를 풀어봅시다.
n=input("괄호 묶음 n을 입력해 주세요.")
stack = []
for i in n:
     if i=="(":
          stack.append(i)
     else: # )
          if stack:
               stack.pop()
          else:
               print("NO")
               break
else:
     if stack: #뭔가 들어있다면
          print("NO")
     else:
          print("YES")
