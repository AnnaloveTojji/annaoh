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
