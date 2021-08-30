print("윤년 프로그램을 시작합니다.")
q=input("윤년 프로그램을 실행하시겠습니까? 네 또는 아니로 대답해 주세요.")
if q=="네":
    print("그럼 시작할게요!")
    yn=int(input("윤년을 감별할 년도를 입력해 주세요."))
    if yn%4==0 and yn%100!=0:
        print("1")
    elif yn%400==0:
        print("1")
    else:
        print("0")
elif q=="아니요":
    print("시스템이 종료 되었습니다.")
