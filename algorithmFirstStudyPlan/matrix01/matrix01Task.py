class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        queue = []
        m = len(mat)
        n = len(mat[0])
        neighbors = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    queue.append([j, i])
                else:
                    mat[i][j] = -1

        while queue:
            x, y = queue.pop(0)  # x - col index, y - row index
            for i in range(4):
                dx, dy = neighbors[i]
                row = y + dy
                col = x + dx
                if col in range(n) and row in range(m) and mat[row][col] == -1:
                    mat[row][col] = mat[y][x] + 1
                    queue.append([col, row])
        return mat


x = Solution()
ans = x.updateMatrix([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
print(ans)
ans = x.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]])
print(ans)
