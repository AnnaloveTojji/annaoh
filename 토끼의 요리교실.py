import random
import time

print("안녕하세요. [토끼의 요리교실]에 오신 것을 환영합니다.")
time.sleep(2)
print("로그인을 진행하셔야 게임을 플레이 할 수 있습니다.")
time.sleep(2)
test_test = int(input("1: appstore 로그인하기 2: naver 로그인하기 3: kakao 로그인하기"))
time.sleep(2)
print("로그인이 완료되었습니다.")
time.sleep(2)

food_list = ["풀떼기 샐러드", "당근 수프", "당근 케이크"]
food = random.choice(food_list)
print(food + "가 요리로 결정되었습니다.")

if food == "당근 케이크":
    ingredient_answer = ["당근", "생크림", "케익 시트", "시럽", "모양 초콜릿"]
    ingredient_wrong_answer = ["바나나", "내 옆에 있는 친구", "아이스크림", "사워크림","핫도그 빵", "식빵", "손 소독제", "핸드폰","소꿉놀이용 당근", "슬라임 피규어"]

time.sleep(2)
print("이 중에서 선생님을 골라주세요.")
time.sleep(2)
teacher_list = ["호랑이 토끼쌤", "토끼 토끼쌤", "물고기 토끼쌤"]
print(teacher_list)
teacher = input("선생님의 이름만 입력해주세요.")

if teacher == "호랑이 토끼쌤":
    print("지금부터 나레이션이 시작됩니다.")
    time.sleep(3)
    print("쾅! 요리교실 문이 갑자기 열렸다.")
    time.sleep(2)
    print("지금부터 요리수업을 시작하겠다! 모두 손은 씻었겠지?")
    time.sleep(2)
    print("너무나 무서운 포스 탓에 나는 무의식적으로 '네'라고 대답했다.")
    time.sleep(2)
    print("그러면 지금부터 " + food + "를 만들어보겠다.")
    time.sleep(2)
    for i in range(5):
        print(str(i + 1) + '번째 재료를 선택해주세요.')
        l = [ingredient_answer[i], ingredient_wrong_answer[i * 2], ingredient_wrong_answer[i * 2 + 1]]
        print(l)
        answer1 = int(input())
