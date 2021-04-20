
# 달팽이는 올라가고 싶다
# https://www.acmicpc.net/problem/2869

# 첫 번째 풀이
a, b, v = map(int, input().split())
total = 0
count = 0
while total <= v:
  count += 1
  total += a
  if total >= v:
    break
  total -= b
print(count)
# while문과 if문 중첩되어 시간 굉장히 오래 걸림

# 두 번째 풀이
a, b, v = map(int, input().split())

if (v-a) % (a-b) == 0:
    x = int((v-a)/(a-b)) + 1
else:
    x = int((v-a)/(a-b)) + 2
print(x)
