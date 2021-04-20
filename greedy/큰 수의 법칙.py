# 큰 수의 법칙
# 다양한 수로 이루어진 배열이 있을 때, 주어진 수들을 M번 더하여 가장 큰 수를 만든다.

# 첫 번째 풀이
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
result = 0
count = 1

data.sort()
while count <= m:
  if count % (k+1) == 0:
    result += data[-2]
    print("count: ", count, "result: ", result)
    count += 1
  else:
    result += data[-1]
    print("count: ", count, "result: ", result)
    count += 1
print(result)
# 반복문 사용으로 시간 초과될 위험 있음

# 두 번째 풀이. 반복되는 수열의 특성을 활용
n, m, k = 5, 8, 3
data = [2, 4, 5, 4, 6]

data.sort()
first = data[-1]
second = data[-2]

# 큰 수 더해지는 횟수 카운트
count = int(m / (k+1)) * k
count += m % (k+1)

# 큰 수 더하기
result = 0
result += first * count

# 두번째 수 더하기
result += second * (m - count)
print(result)
