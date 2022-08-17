class Solution:
    def minimumTotal(self, triangle: list[list[int]]) -> int:
        m = len(triangle)
        for i in reversed(range(m-1)): #идём снизу и считаем минимальные значения для каждого места
            for j in range(len(triangle[i])):
                triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
        return triangle[0][0]


x = Solution()
ans = x.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])
print(ans)
ans = x.minimumTotal([[-10]])
print(ans)
