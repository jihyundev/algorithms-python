
# 미로 탐색
# https://www.acmicpc.net/problem/2178

from collections import deque

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 방향 (상, 하 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))  # 탐색 시작 노드를 큐에 삽입
    while queue:
        print(graph)
        x, y = queue.popleft()  # 큐에서 노드 꺼내기
        for i in range(4):  # 현재 위치에서 네 방향으로의 위치 확인
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 처음 방문하는 경우 최단거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    return graph[n-1][m-1]


print(bfs(0, 0))
