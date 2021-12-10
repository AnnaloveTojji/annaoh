k = int(input())
lst=[]
for i in range(k):
    n = int(input())
    lst.append(n)
for n in lst:
    buttons = [0]*5
    sixties = n // 60
    tens = (n%60) // 10
    ones = n % 10
    if ones > 5:
        tens += 1
        ones -= 10
    if tens > 3:
        sixties += 1
        tens -= 6
    if ones == 5 and tens < 0:
        tens += 1
        ones -= 10
    buttons[0] = sixties
    buttons[2-(tens>0)]=abs(tens)
    if ones > 0:
        buttons[3] = abs(ones)
    else:
        buttons[4] = abs(ones)
    print(*buttons)
