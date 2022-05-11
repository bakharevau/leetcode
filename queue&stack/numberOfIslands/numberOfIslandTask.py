class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        is_visited = [[False for j in range(n)] for i in range(m)]
        island_count = 0

        def findIslang(x, y):
            queue = []
            if x - 1 in range(n) and y in range(m) and not is_visited[y][x - 1]:
                if grid[y][x - 1] == '1':
                    queue.append([x - 1, y])
                    is_visited[y][x - 1] = True
                else:
                    is_visited[y][x - 1] = True

            if x in range(n) and y - 1 in range(m) and not is_visited[y - 1][x]:
                if grid[y - 1][x] == '1':
                    queue.append([x, y - 1])
                    is_visited[y - 1][x] = True
                else:
                    is_visited[y - 1][x] = True

            if x + 1 in range(n) and y in range(m) and not is_visited[y][x + 1]:
                if grid[y][x + 1] == '1':
                    queue.append([x + 1, y])
                    is_visited[y][x + 1] = True
                else:
                    is_visited[y][x + 1] = True

            if x in range(n) and y + 1 in range(m) and not is_visited[y + 1][x]:
                if grid[y + 1][x] == '1':
                    queue.append([x, y + 1])
                    is_visited[y + 1][x] = True
                else:
                    is_visited[y + 1][x] = True
            return queue

        for i in range(m):
            for j in range(n):
                if not is_visited[i][j]:
                    if grid[i][j] == '0':
                        is_visited[i][j] = True
                    else:
                        queue = findIslang(j, i)
                        is_visited[i][j] = True
                        if not len(queue) == 0:
                            while len(queue) > 0:
                                x, y = queue.pop(0)
                                is_visited[y][x] = True
                                queue.extend(findIslang(x, y))
                            island_count += 1
                        else:
                            island_count += 1
        return island_count


x = Solution()
ans = x.numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
])
print(ans)
ans = x.numIslands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
])
print(ans)
ans = x.numIslands([["1", "0", "1", "1", "0", "1", "1"]])
print(ans)
