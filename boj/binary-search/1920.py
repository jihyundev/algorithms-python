
# 1920번 수 찾기
# https://www.acmicpc.net/problem/1920

n = int(input())
a = list(map(int, input().split()))

m = int(input())
tests = list(map(int, input().split()))

def search(key: int, list: list) -> int:
    pl = 0
    pr = len(list) - 1
    while True:
        pc = (pl + pr) // 2
        print(f'pl: {pl}, pr: {pr}, pc: {pc}')
        print("list[pc]:", list[pc])
        if key == list[pc]:
            return 1
        elif key > list[pc]:
            pl = pc + 1
        else:
            pr = pc - 1
        if pl > pr:
            return 0
a.sort()
print("a:", a)
for i in tests:
    result = search(i, a)
    print(result)
