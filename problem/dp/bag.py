"""
背包 挖矿 问题
特点  value weight a(a是上限)
"""

weight = [5, 3, 2, ]
value = [12, 8, 5, ]
a = 5

# value = [400, 200, 300, 350, 500]
# weight = [4, 3, 4, 3, 5]
# a = 10
# f(n, a)=max{f(n-1, a),f(n-1, a-w[i])+v[i]}
# f(n, 0)=0
# f(0, a)=v[0] if w[0] < a else 0
# f(n, a)=f(n-1, a) if a < w[i]

f = [[0 for _ in range(a + 1)] for _ in range(len(weight))]
for i in range(a + 1):
    if weight[0] <= i:
        f[0][i] = value[0]
for i in range(1, len(weight)):
    for j in range(1, a + 1):
        if j < weight[i]:
            f[i][j] = f[i - 1][j]
        else:
            f[i][j] = max(f[i - 1][j], f[i - 1][j - weight[i]] + value[i])

print("f {}".format(f))
