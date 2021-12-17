#Python 강의로 기본기를 잡으세요!
#Python winter 특강!
#쇠막대기
a = list(input("괄호 묶음을 입력해 주세요.")) #문자열을 리스트로 변환 시킨 것 #문자열은 변경 불가능
stack = []
res = 0 #결과를 저장
for i in range(len(a)):
    if a[i] == "(":
        stack.append(i)
    else: #)
        if a[i-1] == "(": #레이저 찾아내기
            stack.pop() #stack을 pop()
            res = res + len(stack) #막대기의 개수만큼 더하기
        else:
            res = res + 1
            stack.pop()
print(res)
