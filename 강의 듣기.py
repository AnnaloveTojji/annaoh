# 2차원 배열의 합
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
memo = [[0]*(m+1) for _ in range(n+1)]  #memoization
print(arr)
print(memo)
for i in range(1, n+1):
    for j in range(1, m+1):
        memo[i][j] = arr[i-1][j-1] + memo[i][j-1] + memo[i-1][j] - memo[i-1][j-1] #memoization 배열에서 값을 합하고, 중복값 빼기
k = int(input())
for _ in range(k):
    i, j, x, y = map(int, input().split())
    print(memo[x][y] - memo[i-1][y] - memo[x][j-1] + memo[i-1][j-1])
    #왜 이렇게 더하고 빼는지 이해하기!
