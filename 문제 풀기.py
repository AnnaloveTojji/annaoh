#1
#print("Hello World")
#2
#print("Mary's cosmetics")
#3
#print("신씨가 소리질렀다. \"도둑이야 !\"")
#4
#print("C:\Windows")
#5
#안녕하세요.
#만나서        반갑습니다.
#6
#오늘은 일요일
#7
#print("naver;kakao;sk;samsung")
#8
#print("naver/kakao/sk/samsung")
#9
#print("first",end="")
#print("second")
#10
#print(5/3)
#11
#삼성전자=50000*10
#print(samsunggunga)
#12
#시가총액="298조"
#현재가=50000
#PER=15.79
#13
#s="hello"
#t="python"
#print(s,end="")
#print("!",end="")
#print(t)
#14
#8
#15
#str
#16
#num_str="720"
#num_str=int(num_str)
#print(num_str)
#17
#num=100
#num=str(num)
#print(num)
#18
#f=15.79
#f=float(f)
#print(type(f))
#19
#year="2020"
#year=int(year)
#print(year-2,year-1,year)
#20
#a=48584
#b=36
#x=a*b
#print(x)
#21
#letters='python'
#print(letters[0],letters[2])
#22
#license_plate="24가 2210"
#license_plate=license_plate[4:]
#print(license_plate)
#23
#string="홀짝홀짝홀짝"
#print(string[::2])
#24
#string="PYTHON"
#print(string[::-1])
#25 (정답확인/replace/배우지 않음)
phone_number="010-1111-2222"
#phone_number=phone_number.replace("-"," ")
print(phone_number)
phone_number=phone_number.replace("-","")
print(phone_number)
#35
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: %s 나이: %d" % (name1, age1))
print("이름: %s 나이: %d" % (name2, age2))
#36
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print("이름: {} 나이: {}".format(name1, age1))
print("이름: {} 나이: {}".format(name2, age2))
#37
name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13
print(f"이름: {name1} 나이: {age1}")
print(f"이름: {name2} 나이: {age2}")
#38
상장주식수 = "5,969,782,550"
컴마제거 = 상장주식수.replace(",", "")
타입변환 = int(컴마제거)
print(타입변환, type(타입변환))
#39
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])
#40
data = "   삼성전자    "
data1 = data.strip()
print(data1)
#41
ticker = "btc_krw"
ticker1 = ticker.upper()
print(ticker1)
#42
ticker = "BTC_KRW"
ticker = ticker.lower()
print(ticker)
#43
a = "hello"
a = a.capitalize()
#44
file_name = "보고서.xlsx"
file_name.endswith("xlsx")
#45
file_name = "보고서.xlsx"
file_name.endswith(("xlsx", "xls"))
#46
file_name = "2020_보고서.xlsx"
file_name.startswith("2020")
#47
a = "hello world"
a.split()
#48
ticker = "btc_krw"
ticker.split("_")
#49
#date = "2020-05-01"
#date=date.split("-")
#print(date)
#50
#data="0039490         "
#data=data.rstrip()
#print(data)
#51
movie_rank=['닥터 스트레인지','스플릿','럭키']
print(movie_rank)
#52
movie_rank=['닥터 스트레인지','스플릿','럭키']
movie_rank.append("배트맨")
#53
movie_rank=['닥터 스트레인지','스플릿','럭키','배트맨']
movie_rank.insert(1,"슈퍼맨")
#54
movie_rank=['닥터 스트레인지','슈퍼맨','럭키','배트맨']
del movie_rank[3]
#55
movie_rank=['닥터 스트레인지','슈퍼맨','배트맨']
del movie_rank[2]
#56
lang1=['C','C++','JAVA']
lang2=['Python','Go','C#']
langs=[]
langs=lang1+lang2
#57
nums=[1,2,3,4,5,6,7]
print("max",max(nums))
print("min",min(nums))
#58
print(sum(nums))
#59
cook=['피자','김밥','만두','양념치킨','족발','피자','김치만두','쫄면','소세지','라면','팥빙수','김치전']
print(len(cook))
#60
nums=[1,2,3,4,5]
print(sum(nums)/len(nums))




















