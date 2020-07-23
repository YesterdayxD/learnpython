
"""
回溯算法的一般思路

result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
"""

# 设置棋盘规模
scale=8

def print_queen():
    for i in Queen:
        print(i)
def find_queen(row):

    if row == scale:
        print_queen()

        print("*******")

        return
    for column in range(scale):
        if check(row,column):
            Queen[row][column]=1
            find_queen(row+1)
            Queen[row][column]=0

def check(row,column):
    for k in range(scale):
        if Queen[k][column] == 1:
            return False

        # 检查主对角线

    for i, j in zip(range(row - 1, -1, -1), range(column - 1, -1, -1)):
        if Queen[i][j] == 1:
            return False

            # 检查副对角线
    for i, j in zip(range(row - 1, -1, -1), range(column + 1, scale)):
        if Queen[i][j] == 1:
            return False

    return True


Queen=[[0 for i in range(scale)] for j in range(scale)]

find_queen(0)
# print_queen()
