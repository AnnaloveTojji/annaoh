#균형잡힌세상
while True:
        a=input()
        if a==".":
                break
        stack=[]
        for i in a:
                if i=="("or i=="[":
                        stack.append(i)
                elif i==")":
                        if stack and stack[-1]=="(":
                                stack.pop()
                        else:
                                stack.append(i)
                elif i=="]":
                        if stack and stack[-1]=="[":
                                stack.pop()
                        else:
                                stack.append(i)
        if stack:
                print("Yes")
        else:
                print("No")
                
