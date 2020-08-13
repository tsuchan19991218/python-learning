N = int(input())
a = list(map(int, input().split()))
dp = [[[0] * (N + 1) for _ in range(N + 1)] for i in range(N + 1)]
for i in range(N + 1):
    for j in range(N + 1):
        for k in range(N + 1):
            dp[i][j][k] = 