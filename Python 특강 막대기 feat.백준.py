import sys
input=sys.stdin.readline
n=int(input())
stack=[int(input()) for i in range(n)]
max=stack[-1]
count=1
for i in range(n):
    temp=stack.pop()
    if temp>max:
        count+=1
        max=temp
print(count)
