import random

masks=input("첫번째 마스크를 입력해줘")
masks2=input("두번째 마스크를 입력해줘")

m=[]
m.append(masks)
m.append(masks2)
print(random.choice(m))
