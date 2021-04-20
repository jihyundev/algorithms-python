# 모험가 길드
# 이코테 p.311
# N명의 모험가에 대한 공포도가 주어졌을 때, 그룹 수의 최댓값 구하기

# 첫 번째 풀이
#n = int(input())
#data = list(map(int, input().split()))
n = 5
data = [2, 3, 1, 2, 2]
data.sort()
count = 0

while True:
  k = data[0]
  max_k = max(data[0:k])
  if max_k > len(data):
    break
  while max_k > k and max_k > len(data):
    max_k = max[data[0:max_k]]
  lst = data[0:max_k]
  data = data[max_k:]
  print("list: ", lst)
  print("data: ", data)
  count += 1
  print("max_k: ", max_k)

print("count: ", count)

# 두 번째 풀이
n = 5
data = [2, 3, 1, 2, 2]
data.sort()
group = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        group += 1
        count = 0
print(group)
