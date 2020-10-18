def huisu(a):
    def dfs(depth, res, path, used, index):
        if index == depth:
            res.append(path[:])
            return
        for i in range(depth):
            if used[i] is not True:
                path.append(a[i])
                used[i] = True
                dfs(depth, res, path, used, index + 1)
                used[i] = False
                path.pop()

    depth = len(a)
    index = 0
    res = []
    path = []
    used = [False for _ in range(depth)]
    dfs(depth, res, path, used, index)
    print(res)


if __name__ == '__main__':
    a = [1, 2, 3]
    huisu(a)
