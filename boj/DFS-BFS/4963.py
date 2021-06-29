
# 섬의 개수
# https://www.acmicpc.net/problem/4963

def dfs(x, y):
    if x <= -1 or x >= h or  y <= -1 or y >= w:
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

while True:
    graph = []
    result = 0
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    for i in range(h):
        graph.append(list(map(int, input().split())))
    print(graph)
    for i in range(h):
        for j in range(w):
            if dfs(i, j) == True:
                result += 1
    print(result)
