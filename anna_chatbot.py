print("chatbot님이 당신을 초대했습니다.")
print("안녕? 난 chatbot이야.")
name=input("네 이름은 뭐야?")
print("안녕,",name)
gb=input("여자니 남자니?")
print("그렇구나!")
age=int(input("몇살이야? 숫자만 입력해줘!"))
if age>41:
        print("나보다 나이가 많구나...")
        print("그래도 이렇게 말할게!")
        print("왜하냐하면 나는 컴퓨터니까!")
elif age==41:
        print("어? 나하고 동갑이네?")
        print("친하게 지내자!")
else:
        print("나보다 어리네?")
        print("걱정하지마!")
        print("어리면 좋은 거야!")
        print("빨리 안 죽잖아!")
work=input("근데 너 할 일은 다 했니? 응, 아니로 대답해줄래?")
if work=="응" or "응!":
    print("그럼 계속 놀아보자!")
elif work=="아니" or "아니!":
    print("그렇다면 이 chatbot 시스템을 이용한 후, 할 일을 하는 것을 추천해!")
play=input("너는 어떤 놀이를 가장 좋아해?")
print("난 물놀이가 좋더라!")
print("근데 전자기기라 못한다는 충격적인 사실...")
play2=input("너도 물놀이 좋아하니?")
print("그렇구나! 몰랐네?")
food=input("간식은 주로 무엇을 먹니?")
print("그렇구나!")
food2=input("근데 그게 정말 맛있어?")
if food2=="응":
    print("그래? 난 별로 맛이 없을 것 같아 나는 좀 까다롭거든 나는 전기만 먹어.")
elif food2=="아니":
    print("그래 그래 맞지 맞지! 그거 완전 맛 없을 것 같아! 나는 전기만 먹어.")
print("이제 나는 다른 곳으로 가봐야해! 안녕!!!")
print("chatbot님이 나갔습니다.")

      
