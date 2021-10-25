#통계값
import statistics
import math
a=[]
b=int(input("몇개의 수를 입력할 건지 입력해줘."))
for c in range(b):
     d=int(input("숫자를 입력해줘"))
     a.append(d)
e=sum(a)
f=e/b
g= b/2
h=math.floor(g)
i=statistics.mode(a)
j=max(a)
k=min(a)
print(round(f))
print(sorted(a)[h])
print(i)
print(j-k)
