# LIS O(n^2)版本
# todo 添加O(nlogn)版本
data = [1, 7, 6, 2, 3, 4]
dp = [1] * len(data)

for i in range(len(data)):
    for j in range(i):
        if data[j] < data[i] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
print(dp)
# 工人挖矿
G = [400, 200, 300, 350, 500]
P = [4, 3, 4, 3, 5]
# F = [0] * len(G)
w = 10
# F(i, w)=max{ F(i-1, w), F(i-1, w-P[i]) + G[i] }
F = [[0 for i in range(w)] for j in range(len(G))]
print(F)

# init
# F[0][w]=0 当w<p[0]
#        =G[0] 当w>=p[0]
for j in range(w):
    if j >= P[0]:
        F[0][j] = G[0]

# F[i][0]=0

for i in range(1, len(G)):
    for j in range(1, w):
        if j < P[i]:
            F[i][j] = F[i - 1][j]
        else:
            F[i][j] = max(F[i - 1][j], F[i - 1][j - P[i]] + G[i])
print(F)
