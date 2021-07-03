
# 섬의 개수
# https://www.acmicpc.net/problem/4963

def dfs(x, y):
    # 주어진 범위를 벗어나는 경우 즉시 종료
    if x <= -1 or x >= h or y <= -1 or y >= w:
        return False
    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 1:
        # 해당 노드 방문 처리
        graph[x][y] = 0
        # 상, 하, 좌, 우, 대각선 위치 재귀적으로 호출
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
    # 입력의 마지막 줄에 대한 예외 처리
    if w == 0 and h == 0:
        break
    for i in range(h):
        graph.append(list(map(int, input().split())))
    print(graph)
    for i in range(h):
        for j in range(w):
            # 현재 위치에서 DFS 수행
            if dfs(i, j) == True:
                result += 1
    print(result)
