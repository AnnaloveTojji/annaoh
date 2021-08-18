#단어공부
word=list(input("단어를 입력해줘"))
l=[]
for i in range(97,123):
    l.append(word.count(chr(i)))
x=len(l)
m=l[0]
for i in range(x):
    if m<l[i]:
        m=l[i]
    else:
        m=m
for i in l:
    if i == m:
        y=l.index(i)
if l.count(m) > 1:
    print("?")
else:
    print(chr(y+97))
