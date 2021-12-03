#PYTHON 특강
#선생님: 오주현
#5강
#백준 사이트 또는 책을 준비하세요~
#17614번 검색 바랍니다~
#369
last_number = int(input("가장 마지막 숫자를 입력해 주세요."))
count=0
for i in range(last_number+1):
    if "3" in str(i):
        count=count+str(i).count("3")
    if "6" in str(i):
        count=count+str(i).count("6")
    if "9" in str(i):
        count=count+str(i).count("9")
print(count)
