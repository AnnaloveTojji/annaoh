def is_palindrome(s):
    return s == s[ : :-1]
def almost_palindrome(s):
    for i in range(len(s)):
        new_string = s[ :i]+s[i+1: ]
        result = is_palindrome(new_string)
        if result == True:
            return result
    return False
t = int(input())
lst=[]
for _ in range(t):
    s = input()
    lst.append(s)
for s in lst:
    result = is_palindrome(s)
    if result == True:
        print(0)
    else:
        result = almost_palindrome(s)
        if result == True:
            print(1)
        else:
            print(2)
