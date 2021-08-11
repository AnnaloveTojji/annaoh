while True:
    a=int(input("첫 번째 숫자를 입력해주세요."))
    b=int(input("두 번째 숫자를 입력해주세요."))
    c=int(input("세 번째 숫자를 입력해주세요."))
    if type(a)==int and type(b)==int and type(c)==int:
        break
x=a*b*c
print("예시를 보여드리겠습니다.")
print("3 2 6 7 4 9 8 1 5 5")
print("0은 3개, 1은 2개, 2는 6개...")
my_list=list(str(x))
for i in range(10):
    print(my_list.count(str(i)))

