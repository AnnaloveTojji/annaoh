def solution(n, lost, reserve):
    u = [1] * (n+2)
    for i in lost:
        u[i] -= 1
    for i in reserve:
        u[i] += 1
    for i in range(1, n+1):
        if u[i]==2 and u[i-1]==0:
            u[i]=u[i-1]=1
        elif u[i]==2 and u[i+1]==0:
            u[i]=u[i+1]=1
    return len([x for x in u[1:-1] if x > 0])
