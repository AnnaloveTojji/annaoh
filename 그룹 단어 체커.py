#그룹 단어 체커
#11-w-d-g-o
a=input("당장 단어 입력해!")
b=list(a)
x=len(b)-1
for i in range(x):
    if b[i] in b[i+1:]:
        print("그룹 단어가 아니예요!")
        break
    else:
        print("그룹 단어예요!")
        break
