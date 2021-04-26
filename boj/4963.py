
# 섬의 개수
# https://www.acmicpc.net/problem/4963

w, h = 5, 4
graph = [[1, 1, 1, 0, 0],
         [1, 0, 1, 0, 0],
         [1, 0, 1, 0, 1],
         [1, 0, 1, 1, 1]]
def dfs(x, y):
    if x <= -1 or x >= h or y <= -1 or y >= w:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x-1, y)
        dfs(x-1, y-1)
        dfs(x-1, y+1)
        dfs(x+1, y)
        dfs(x+1, y-1)
        dfs(x+1, y+1)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False
result = 0
for i in range(h):
    for j in range(w):
        if dfs(i, j) == True:
            result += 1
print(result)
