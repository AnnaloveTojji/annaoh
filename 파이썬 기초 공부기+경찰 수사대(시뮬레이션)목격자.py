bill=list(map(int,input("식탁에 있던 모든 음식의 가격을 각각 말씀해주세요.").split()))
print("잘 하셨습니다!")
print("이 내용은 수사에 도움이 될 것 입니다.")
k=int(input("anna가 먹지 않은 음식의 가격 인덱스를 말씀해주세요."))
print("좋습니다.")
print("한 가지 더 물어보겠습니다.")
b=int(input("brian이 anna에게 얼마를 돌려주라고 하였나요?"))
print("감사합니다.")
print("큰 도움이 되었습니다.")
check=int(input("혹시 시간이 괜찮으시다면 저희 수사과정을 구경하시겠습니까? '네'는 1, '아니요'는 2를 말씀해주세요."))
if check==1:
    print("네 알겠습니다.")
    print("수사 과정은 비밀리에 진행되오니 언급을 삼가해주시기 바랍니다.")
    print("이제 가시죠!")
    doing1=sum(bill)-bill[k]
    print("저희가 수사를 할 동안에는 지구대를 한번 둘러보세요.")
    doing2=doing1/2
    print("이 간식 좀 드세요.")
    if b==doing2:
        print("판정을 내겠습니다.")
        print("법사님 나오십니다.")
        print("brian이 맞는 대답을 하였습니다.")
        print("anna는 그 돈의 2배를 물어내세요.")
    elif b!=doing2:
        print("anna가 맞습니다.")
        c=b-doing2
        print(c)
