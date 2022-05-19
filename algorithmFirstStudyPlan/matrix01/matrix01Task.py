class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        queue = []
        m = len(mat)
        n = len(mat[0])

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append([j, i])
                else:
                    mat[i][j] = -1

        while queue:
            x, y = queue.pop(0)  # x - col index, y - row index
            if x + 1 in range(n) and y in range(m) and mat[y][x + 1] == -1:
                mat[y][x + 1] = mat[y][x] + 1
                queue.append([x + 1, y])
            if x in range(n) and y + 1 in range(m) and mat[y + 1][x] == -1:
                mat[y + 1][x] = mat[y][x] + 1
                queue.append([x, y + 1])
            if x - 1 in range(n) and y in range(m) and mat[y][x - 1] == -1:
                mat[y][x - 1] = mat[y][x] + 1
                queue.append([x - 1, y])
            if x in range(n) and y - 1 in range(m) and mat[y - 1][x] == -1:
                mat[y - 1][x] = mat[y][x] + 1
                queue.append([x, y - 1])

        return mat


x = Solution()
ans = x.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
print(ans)
ans = x.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]])
print(ans)
