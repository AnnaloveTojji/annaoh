n = int(input())
count = 0
for i in range(1, n+1):
    str_n = str(i)
    counted1 = str_n.count('3')
    count += counted1
    counted2 = str_n.count('6')
    count += counted2
    counted3 = str_n.count('9')
    count += counted3
print(count)
