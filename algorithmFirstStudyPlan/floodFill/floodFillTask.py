class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
        curr_x, curr_y = sc, sr
        m = len(image)
        n = len(image[0])
        is_checked = [[False for i in range(n)] for j in range(m)]
        prevColor = image[sr][sc]

        def paintCell(x, y):
            is_checked[y][x] = True
            image[y][x] = newColor
            if x - 1 in range(n) and y in range(m) and not is_checked[y][x - 1] and image[y][x - 1] == prevColor:  # left neighbor
                paintCell(x-1, y)

            if x in range(n) and y - 1 in range(m) and not is_checked[y - 1][x] and image[y - 1][x] == prevColor:  # upper neighbor
                paintCell(x, y-1)

            if x + 1 in range(n) and y in range(m) and not is_checked[y][x + 1] and image[y][x + 1] == prevColor:  # right neighbor
                paintCell(x+1, y)

            if x in range(n) and y + 1 in range(m) and not is_checked[y + 1][x] and image[y + 1][x] == prevColor:  # down neighbor
                paintCell(x, y+1)

        paintCell(curr_x, curr_y)
        return image


x = Solution()
ans = x.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2)
print(ans)

ans = x.floodFill([[0, 0, 0], [0, 0, 0]], 0, 0, 2)
print(ans)