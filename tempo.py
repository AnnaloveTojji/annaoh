#최대공약수
def calculate_gcd(x,y):
    small_list=[x,y]
    small=min(small_list)
    i=2
    while True:
        if x%i==0 and y%i==0:
            gcd=i
        i=i+1
        if i>small:
            break
    return gcd
a=int(input("a: "))
b=int(input("b: "))
print(calculate_gcd(a,b))
