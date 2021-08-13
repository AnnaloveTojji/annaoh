print("단어를 입력하다 그만하고 싶으시면 0을 눌러주세요. 단어를 입력할 차례에 0을 누르고 엔터를 쳐주세요")
taja=["가위","저녁","가여움","아기","지우개","그림","개미","컴퓨터","시계","아이패드","종이","마우스","전선","노트","물티슈","칠판","책장","텔레비전","나무","컵","액자","공기청정기","가방","에어컨","쓰레기통","비닐장갑","문","학원","건물","아이스크림","토끼","호랑이","꽃","냉장고","번호","사물함","하늘","새","비행기","기차","자동차","종이컵","물","도자기","수학","학교","줄무늬","원소","중복","제거"]
def my_skunk(taja):
    for i in taja:
        print(i)
        e=input()
        if e=="0":
            break
        elif i!=e:
            print("다시해")
            print(i)
            e=input()
        elif i!=e:
            print("너는 그냥 다음거 해")
            print("너는 글렀어")
my_skunk(taja)
print("다음은 영어입니다")
taja2=["dog","cat","mouse","pen","pencile","high","kiwi","face","world","numbers","night","diver","police","lake","knownledge","chest","oven","mud","union","mom","recipe","way","meal","girl","thanks","classroom","engine","person","lab","country","girlfriend","volume","student","add","history","birthday","world","beer","writher","shirt","people","tea","scene","height","user","disaster","player","refrigerator","dirt","restaurant"]
my_skunk(taja2)
print("종료!")
