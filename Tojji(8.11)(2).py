while True:
    a=input("O와 X를 영어 대문자로 입력해주세요. 열 개 모두 띄어쓰기로 입력해주세요.")
    if 'O' and 'X' in a:
        break
mylist=list(a)
mylist2=a.split('X')
print(mylist2)
love=0
for i in mylist2:
    x=len(i )
    print(x)
    for d in range(x+1):
        love=love+d
        print(d)
print(love)
#해킹 수업
#
