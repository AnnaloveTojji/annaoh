import random
print("안녕하십니까? 오&세이 회사에서 만들어진 이상한 나라입니다.")
print("이용하실 서비스를 선택해주세요.")
service=int(input("이상한 나라의 계산기 서비스를 이용하시려면 1을, 아이 스토리 서비스를 이용하시려면 2를, 종료하시려면 3을 입력해주세요."))
if service==1:
    print("이상한 나라의 계산기 서비스를 시작합니다.")
    print("로딩중...")
    print("숫자를 불러오는 중...")
    print("이상한 나라로 들어가는 중...")
    print("불러오는 중...")
    print("warning! 이 프로그램의 부호는 더하기로 한정되어 있습니다.")
    number1=int(input("한 자리 수를 입력해주세요."))
    number2=int(input("한 자리 수를 입력해주세요."))
    while True:
        random1=random.randint(1,11)
        if random1!=number1+number2:
            break
    print("hello")
