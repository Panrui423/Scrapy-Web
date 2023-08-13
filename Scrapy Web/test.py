


res = []
def printPaths(mat, route=[], i=0, j=0):
    # 基础案例
    if not mat or not len(mat):
        return

    # `M × N`矩阵
    (M, N) = (len(mat), len(mat[0]))

    # 在路由中包含当前单元
    route.append(mat[i][j])

    # 如果到达最后一个单元格，则为
    if i == M - 1 and j == N - 1:
        print(route)
    else:
        # 下移
        if i + 1 < M:
            printPaths(mat, route, i + 1, j)

        # 右移
        if j + 1 < N:
            printPaths(mat, route, i, j + 1)

    # 回溯：从路由中移除当前单元格
    route.pop()


if __name__ == '__main__':
    mat = [
        [1, 2, 3, 4],
        [4, 5, 6, 7],
        [7, 8, 9, 10]
    ]

    printPaths(mat)
    print(res)


