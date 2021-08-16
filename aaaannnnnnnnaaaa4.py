print("알파벳 찾기를 시작합니다")
word=input("영어 단어를 입력해주세요")
for i in range(ord('a'),ord('z')+1):
    print(word.find(chr(i)),end="")
    
