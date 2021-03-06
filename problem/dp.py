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
# todo 有问题
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
"""
最大子序和
"""
data = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


def max_sub_array(a):
    f = len(a) * [0]
    f[0] = a[0]
    result = f[0]
    for i in range(1, len(a)):
        f[i] = a[i] + max(f[i - 1], 0)
        result = max(f[i], result)
    return result


print(max_sub_array(data))

"""
最小编辑距离
"""
str1 = ""
str2 = ""


def min_edit_distance(str1, str2):
    I = len(str1) + 1
    J = len(str2) + 1
    dp = [[0 for _ in range(J)] for _ in range(I)]
    print(dp)
    for i in range(I):
        dp[i][0] = i
    for j in range(J):
        dp[0][j] = j
    for i in range(1, I):
        for j in range(1, J):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1],
                               dp[i - 1][j - 1]) + 1
                # print(dp[i][j])
    return dp[I - 1][J - 1]


"""
bag
"""
weight = [3, 2, 5]
value = [8, 5, 12]
a = 5
# f(n, a)=max{f(n-1, a),f(n-1, a-w[i])+v[i]}
# f(n, 0)=0
# f(0, a)=v[0] if w[0] < a else 0
# f(n, a)=f(n-1, a) if a < w[i]

f = [[0 for _ in range(a)] for _ in range(len(weight))]
for i in range(a):
    if weight[0] < i:
        f[0][i] = value[0]
print("f {}".format(f))

if __name__ == '__main__':
    # print(min_edit_distance("horse", "h"))
    pass
