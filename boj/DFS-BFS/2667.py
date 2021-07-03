
# 단지번호붙이기
# https://www.acmicpc.net/problem/2667

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

count = 0  # 단지 내 집의 수 세는 전역 변수


def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n or graph[x][y] == 0:
        return -1
    else:  # graph[x][y] == 1인 경우
        graph[x][y] = 0
        global count
        count += 1
        # 상, 하, 좌, 우 재귀적으로 호출
        dfs(x-1, y)  # 리턴될 경우 다음 dfs 호출
        dfs(x+1, y)
        dfs(x, y+1)
        dfs(x, y-1)
        return count


blocks = 0  # 단지 수
houses = []  # 각 단지 내 집의 수

for i in range(n):
    for j in range(n):
        result = dfs(i, j)
        count = 0  # 전역변수 초기화
        if result != -1:
            blocks += 1
            houses.append(result)
print(blocks)
for house in houses:
    print(house)
# 채점 결과 틀렸음 ㅠㅠ
