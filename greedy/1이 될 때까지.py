# N이 1이 될 때까지 연산하는 최소 횟수 구하기
# 연산의 종류는 1. 1을 빼거나 2. K로 나누기만 가능

# 첫 번째 풀이
n, k = 17, 4
count = 0

while n != 1:
    if n % k == 0:
        n = n // k
        count += 1
    else:
        n -= 1
        count += 1
print(count)

n, k = 17, 4
count = 0
# 두 번째 풀이
while True:
    # N이 K로 나누어 떨어질 수 있을 때까지 1씩 빼기
    target = (n // k) * k
    count += (n - target)
    n = target
    # N이 K보다 작을 땐 반복문 탈출
    if n < k:
        break
    # K로 나누기
    n = n // k
    count += 1
count += (n-1)
print(count)
