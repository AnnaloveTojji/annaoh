#세로 읽기
words=[input() for i in range(5)]
m = len(max(words,key=len))
for i in range(m):
        for j in range(5):
                if i>=len(words[j]):
                        continue
                else:
                        print(words[j][i],end='')
