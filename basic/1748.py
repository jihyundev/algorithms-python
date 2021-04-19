
# 수 이어쓰기 1
# https://www.acmicpc.net/problem/1748

def solution(n):
    ret = 0
    for i in range(1, n+1):
        q = i // 10
        if q == 0:
            ret = ret * 10 + i
            i += 1
        elif 1 <= q < 10:
            ret = ret * (10 ** 2) + i
            i += 1
        elif 10 <= q < 100:
            ret = ret * (10 ** 3) + i
            i += 1
        elif 100 <= q < 1000:
            ret = ret * (10 ** 4) + i
            i += 1
        else:
            ret = 0
    return len(str(ret))
# 비효율적인 코드. 길이값만 구하면 되는데 전체 결과값을 한차례 구한 다음에 길이를 구하려고 하기 때문

def solution1(n):
    ret = 0
    for i in range(1, n+1):
        ret += len(str(i))
    return ret
# 최대 입력 값이 1억. n번 동안 iteration을 해야 하므로 마찬가지로 매우 오랜 시간이 걸린다.

def solution2(n):
    l, ret = len(str(n)), 0
    for i in range(1, l):
        ret += i * (10**i - 10**(i-1))
    ret += l * (n - 10 ** (l-1) + 1)
    return ret
# 자릿수 만큼만의 iteration으로 결과값을 구할 수 있음.


print(solution2(100000000))
