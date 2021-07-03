
# 유기농 배추
# https://www.acmicpc.net/problem/1012

import sys
sys.setrecursionlimit(10**6)

m, n = 1, 1


def dfs(x, y):
    # 주어진 범위를 벗어나는 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 1:
        # 해당 노드 방문 처리
        graph[x][y] = 0
        # 상, 하, 좌, 우 재귀적으로 호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return True
    return False


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]  # 그래프 초기화
    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    result = 0
    for i in range(n):
        for j in range(m):
            # 현재 위치에서 DFS 수행
            if dfs(i, j) == True:
                result += 1
    print(result)
